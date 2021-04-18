import speech_recognition as sr
import pyttsx3 as p
import time
from horario import hours
from dia import day
from crypto import findPriceCoin
from clima import findcity
import inspect

keywords = ['dia', 'horas', 'clima', 'preço']
functions = {
    'dia': day,
    'horas': hours,
    'clima': findcity,
    'preço': findPriceCoin
}

remove = 'lua'

r = sr.Recognizer()
m = sr.Microphone()
engine = p.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen(m):
    with m as source:
        audio = r.listen(source, phrase_time_limit=60)
    try:
        voice = r.recognize_google(audio, language="pt-BR")
        voice = voice.lower()
        if 'lua' in voice:
            tratamento(voice)
    except sr.UnknownValueError:
        print('Não consegui te entender. Por favor, poderia repetir?')

def tratamento(voice):
    remove_cmd = voice.replace('lua', '')
    trat_voice = remove_cmd.split()
    call_command(trat_voice, remove_cmd)

def call_command(trat_voice, remove_cmd):
    print(trat_voice)
    for command in keywords:
        if command in trat_voice:
            select_key =  command
            arguments = inspect.getfullargspec(functions[select_key]).args
            arguments_length = len(arguments)
            
            if arguments_length >= 1:
                functions[select_key](remove_cmd)
            if arguments_length == 0:
                functions[select_key]()
            else:
                talk('Comando não encontrado... Por favor, tente novamente')
                print('Comando não encontrado... Por favor, tente novamente')

while True:
    listen(m)
    time.sleep(1)