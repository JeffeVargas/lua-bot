import datetime
import calendar
import pyttsx3 as p

engine = p.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def dia():
    list_mes = {
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
    list_semana = {
        'Monday' : 'Segunda-feira',
        'Tuesday' : 'Terça-feira',
        'Wednesday' : 'Quarta-feira',
        'Thursday' : 'Quinta-feira',
        'Friday' : 'Sexta-feira',
        'Saturday' : 'Sábado',
        'Sunday' : 'Domingo'
    }
    time = datetime.datetime.now()
    ano = time.strftime('%Y')
    mes = time.strftime('%B')
    semana = time.strftime('%A')
    dia = time.strftime('%d')

    talk(f'{list_semana[semana]}, dia {dia} do mês de {list_mes[mes]} e do ano de {ano}')