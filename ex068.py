#Faça um programa que jogue par ou ímpar com o computador.
#  O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

print("=-"*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print("=-"*20)

count = 0

while True:
    n = int(input('Informe o valor: '))
    # opcao = input('Par ou Ímpar [P/I]: ').strip().upper()
    opcao = ' '
    computador = randint(0,10)
    # print(computador)
    soma = n + computador
    while opcao not in 'PI':
        opcao = input('Par ou Ímpar [P/I]: ').strip().upper()[0]
    print('Voce jogou {} e o computador {}. Total de {} '.format(n, computador,soma), end='')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if opcao == 'P':
        if soma % 2 == 0:
            print('Você GANHOUR')
            count += 1
        else:
            print('Você PERDEU')
            break
    elif opcao == 'I':
        if soma % 2 == 0:
            print('você GANHOU')
            count += 1
        else:
            print('Você PERDEU')
            break
    print('Vmos jogar novamente...')

print('GAME OVER! Você venceu {} vezes'.format(count))
# soma = n + computador
# par = soma % 2 == 0

# if soma % 2 == 0:
#     if opcao == 'P':
#         print('Voce jogou {} e o computador{}. Total de {} DEU PAR'.format(n, computador,soma))
#         print('Você GANHOUR')
#     else:
#         print('Voce jogou {} e o computador{}. Total de {} DEU PAR'.format(n, computador,soma))
#         print('Você PERDEU')
# else:
#     print('Voce jogou {} e o computador{}. Total de {} DEU ÍMPAR'.format(n, computador,soma))

# print('GAME OVER!')


