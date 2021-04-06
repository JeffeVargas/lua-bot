import datetime
import calendar
import pyttsx3 as p

engine = p.init()
horas = False

def talk(text):
    engine.say(text)
    engine.runAndWait()

def horas():
    time = datetime.datetime.now()
    time = time.strftime('%H:%M')
    talk(f'Agora são {time}')
