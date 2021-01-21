import os

pipv = str(input('Você utiliza pip ou pip3? '))
if pipv == 'pip':
    os.system('pip install speechrecognition')
    os.system('pip install pyttsx3')
    os.system('pip install selenium')
    os.system('pip install webdriver-manager')
    os.system('pip install pyaudio')
    exit()
if pipv == 'pip3':
    os.system('pip3 install speechrecognition')
    os.system('pip3 install pyttsx3')
    os.system('pip3 install selenium')
    os.system('pip3 install webdriver-manager')
    os.system('pip3 install pyaudio')
    exit()
else:
    print('Opção inválida!')
