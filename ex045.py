#Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep


itens = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0,2)
#print('O computador jogou: '.format(intens[computador]))
print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador =  int(input('Qual é a sua jogada: '))
sleep(1)
print('-=' * 11)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence!')
    elif jogador == 2:
        print('Computador Vence!')
    else:
        print('Jogada inválida!')

elif computador == 1:
    if jogador == 0:
        print('Computador Vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador Vence')
    else:
        print('Jogada inválida')

elif computador == 2:
    if jogador == 0:
        print('Jogador vence!')
    elif jogador == 1:
        print('Computador Vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')