#criar um app de chamada cujo objetivo é armazenar o nome de cada aluno,matricula e data,
# e enviar via email,whatsapp ou sms com todos os alunos presentes.
import smtplib
import time
from datetime import datetime
from email.message import EmailMessage

from loginemail import senha

tm=datetime.now()
tempo=datetime.now().strftime('%d/%m/%Y')
hora = tm.strftime("%H: %M: %S")
dia_semana = tm.strftime('%A')
dia = tm.day
mes = tm.strftime('%b')
ano = tm.strftime('%Y')

#Materias e seus Respectivos Dias.

segunda = 'Praticas Extensionistas'
terça = 'Expressão Gráfica'
quarta = 'Introdução a Química'
quinta = 'Resoluções de Problemas para engenharia I'
sexta = 'Pensamento Computacional'
sabado = 'Introdução a Engenharia'

time.sleep(1.0)
inicio = print(hora)
time.sleep(1.0)
if dia_semana == 'Monday' or dia_semana == 'segunda-feira':
    print('='*80)
    title = print(f'Lista de Presença virtual-{segunda}')
    print('=' * 80)
if dia_semana == 'Tuesday' or dia_semana == 'terça-feira':
    print('=' * 80)
    title = print(f'Lista de Presença virtual-{terça}')
    print('=' * 80)
if dia_semana == 'Wednesday' or dia_semana == 'quarta-feira':
    print('=' * 80)
    title = print(f'Lista de Presença virtual-{quarta}')
    print('=' * 80)
if dia_semana == 'Thursday' or dia_semana == 'quinta-feira':
    print('=' * 80)
    title = print(f'Lista de Presença virtual-{quinta}')
    print('=' * 80)
if dia_semana == 'Friday' or dia_semana == 'sexta-feira':
    print('=' * 80)
    title = print(f'Lista de Presença virtual-{sexta}')
    print('=' * 80)
if dia_semana == 'Saturday' or dia_semana == 'sábado':
    print('=' * 80)
    title = print(f'Lista de Presença virtual-{sabado}')
    print('=' * 80)
time.sleep(1.5)
list_nome = []

def listpv() :
    nome = input('Digite seu nome Completo: ')
    list_nome.append(nome)
while True:
    listpv()
    end = str(input('Press Enter '))
    if end == 'encerrar' or end == 'ENCERRAR':
        break

msg1 = f"""   
<p> Lista de Presença virtual {tempo} </p>

 <p>{list_nome}</p>
"""
    # email, senha.
EMAIL_ADDRESS = 'chamadaprova2@hotmail.com'
EMAIL_PASSWORD = senha

msg = EmailMessage()
msg['Subject'] = (f'Lista de Presença virtual{tempo}')
msg['From'] = 'chamadaprova2@hotmail.com'
msg['To'] = 'paaulomsf@gmail.com'
msg.set_content(msg1)
with smtplib.SMTP_SSL('smtp.office365.com', 587) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print('email enviado')
