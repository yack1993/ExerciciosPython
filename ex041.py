# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER
from datetime import date
anoAtual = date.today().year
nasc = int(input('Ano de nascimento: '))
ano = anoAtual - nasc

if(ano <= 9):
    print('O atleta tem {}'.format(ano))
    print('Classificação: MIRIM')
elif ano <= 14:
    print('O atleta tem {}'.format(ano))
    print('Classificação: MIRIM')
elif ano <= 19:
    print('O atleta tem {}'.format(ano))
    print('Classificação: JÚNIOR')
elif ano <= 25:
    print('O atleta tem {}'.format(ano))
    print('Classificação: SÊNIOR')

elif ano > 25:
    print('O atleta tem {}'.format(ano))
    print('Classificação: MASTER')

