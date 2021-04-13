import speech_recognition as sr
import pyttsx3 as p
import time
from horario import horas
from dia import dia
from dollar import doll
from crypto import bat
from clima import findcity

keywords = ['dia', 'horas', 'dólar', 'clima', 'bat']
functions = {
    'dia': dia,
    'horas': horas,
    'dólar': doll,
    'clima': findcity,
    'bat': bat
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
    trat_voice = voice.replace('lua', '')
    call_command(trat_voice)

def call_command(trat_voice):
    for i in keywords:
        if 'clima' in trat_voice:
            functions['clima'](trat_voice=trat_voice)
            break
        else:
            talk('Comando não encontrado... Tente algum comando válido')
            print('Comando não encontrado... Tente algum comando válido')
            break

        if i in trat_voice:
            functions[i]()
        else:
            talk('Comando não encontrado... Tente algum comando válido')
            print('Comando não encontrado... Tente algum comando válido')
            break

while True:
    listen(m)
    time.sleep(1)
