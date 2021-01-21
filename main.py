import speech_recognition as sr
import pyttsx3 as p
import datas
import whatsapp

r = sr.Recognizer()
engine = p.init()
remove = ['lua', 'no whatsapp']

def talk(text):
    engine.say(text)
    engine.runAndWait()

def hear():
    with sr.Microphone() as lua_source:
        listen = r.listen(lua_source)
        speech_to_text(listen)

def speech_to_text(listen):
    try:
        stt = r.recognize_google(listen, language='pt-BR')
        stt = stt.lower()
        print(stt)
        if 'lua' in stt:
            call_command(stt)
        else:
            pass
    except:
        print('Erro desconhecido')

def tratamento(stt):
    for i in remove:
        stt = stt.replace(i, '')

    stt_splited = stt.split(' ')

    message = []
    name = []
    time = []

    controller1 = False
    controller2 = False
    controller3 = False

    for i in stt_splited:
        if i == 'para':
            controller1 = False

        if i == 'escreva' or controller1:
            controller1 = True
            if i != 'escreva':
                message.append(i)

        if i == 'e':
            controller2 = False

        if i == 'para' or controller2:
            controller2 = True
            if i != 'para':
                name.append(i)

        if i == 'no':
            controller3 = False

        if i == 'às' or controller3:
            controller3 = True
            if i != 'às':
                time.append(i)

    whatsapp.whatsapp(''.join(name), ''.join(message), ''.join(time))

def call_command(stt):
    keywords = {
        'que dia' : datas.dia,
        'que horas' : datas.horas,
        'whatsapp' : tratamento
    }
    a = get_command(stt, keywords)
    if a == 'whatsapp':
        tratamento(stt)
    if a != False:
        keywords[a]()

def get_command(stt, keywords):
    for i in keywords.keys():
        if i in stt:
            return i
    return False

while True:
    hear()
