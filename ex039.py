# Faça um programa que leia o ano de nascimento de um jovem e informe, 
 #de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
 #se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
 # Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nasc = int(input('Informe o ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, anoatual))
if idade < 18:
    saldo = 18 - idade
    ano = anoatual + saldo
    print('Ainda Faltam {} para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    ano = anoatual - saldo
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))
