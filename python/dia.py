import datetime
import calendar
import pyttsx3 as p

engine = p.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def day():
    month_list = {
        'January' : 'Janeiro',
        'February' : 'Fevereiro',
        'March' : 'Março',
        'April' : 'Abril',
        'May' : 'Maio',
        'June' : 'Junho',
        'July' : 'Julho',
        'August' : 'Agosto',
        'September' : 'Setembro',
        'October' : 'Outubro',
        'November' : 'Novembro',
        'December' : 'Dezembro'
    }
    week_list = {
        'Monday' : 'Segunda-feira',
        'Tuesday' : 'Terça-feira',
        'Wednesday' : 'Quarta-feira',
        'Thursday' : 'Quinta-feira',
        'Friday' : 'Sexta-feira',
        'Saturday' : 'Sábado',
        'Sunday' : 'Domingo'
    }
    time = datetime.datetime.now()
    year = time.strftime('%Y')
    month = time.strftime('%B')
    week = time.strftime('%A')
    today = time.strftime('%d')

    talk(f'{week_list[week]}, dia {today} do mês de {month_list[month]} e do ano de {year}')