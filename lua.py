import speech_recognition as sr
import pyttsx3 as p
import time
from horario import horas
from dia import dia
from dollar import doll
from crypto import bat
from clima import weather

keywords = ['dia', 'horas', 'dólar', 'clima', 'bat']
functions = {
    'dia': dia,
    'horas': horas,
    'dólar': doll,
    'clima': weather,
    'bat': bat
}

remove = 'lua'
r = sr.Recognizer()
m = sr.Microphone()

def listen(m):
    with m as source:
        audio = r.listen(source, phrase_time_limit=60)
    try:
        voice = r.recognize_google(audio, language="pt-BR")
        voice = voice.lower()
        if 'lua' in voice:
            tratamento(voice)
    except sr.UnknownValueError:
        print('Erro desconhecido')

def tratamento(voice):
    trat_voice = voice.replace('lua', '')
    call_command(trat_voice)

def call_command(trat_voice):
    for i in keywords:
        if 'clima' in trat_voice:
            functions['clima'](city=trat_voice)
            break

        if i in trat_voice:
            functions[i]()


while True:
    listen(m)
    time.sleep(1)
