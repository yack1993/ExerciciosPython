#Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


opcao = 'S'
count = 0
media = 0
soma = 0
maior_menor = []

while opcao != 'N':
    n = int(input('Informe um número: '))
    maior_menor.append(n)
    soma = soma + n
    count += 1
    media = soma / count
    opcao = input('Quer continuar? [S/N]: ').strip().upper()
print('Você digitou {} números e a média é {:.2f}'.format(count, media))
print('O maior valor é {} e o menor é {}'.format(max(maior_menor), min(maior_menor)))


