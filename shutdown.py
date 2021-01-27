import os
import datetime
import pyttsx3 as p

engine = p.init()

class shutdown():

    def convert(tempo):
        tempo = (tempo*60)*60

    def __init__(tempo):
        while True:

            now = datetime.datetime.now()
            time = now.strftime('%H:%M')
            if time == shutdown:
                os.system(f"shutdown /s /t {tempo}")
                break