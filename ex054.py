 #Crie um programa que leia o ano de nascimento de sete pessoas. 
 # No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.)
from datetime import date

ano_atual = date.today().year
maior = 0
menor  = 0

ano1 = int(input('Informe o ano que a 1ª pessoa nasceu: '))
ano2 = int(input('Informe o ano que a 2ª pessoa nasceu: '))
ano3 = int(input('Informe o ano que a 3ª pessoa nasceu: '))
ano4 = int(input('Informe o ano que a 4ª pessoa nasceu: '))
ano5 = int(input('Informe o ano que a 5ª pessoa nasceu: '))
ano6 = int(input('Informe o ano que a 6ª pessoa nasceu: '))
ano7 = int(input('Informe o ano que a 7ª pessoa nasceu: '))

lista = [ano1, ano2, ano3, ano4, ano5, ano6, ano7]

for i in lista:
    if (ano_atual - i) >= 18:
        maior += 1
    else:
       menor += 1
print('Ao todo tivemos {} pessoas maiores de idade!'.format(maior))
print('E também tivemos {} pessoas menores de idade!'.format(menor))