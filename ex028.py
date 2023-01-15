#Escreva um programa que faça o computador "pensar" em um número 
# inteiro entre 0 e 5 e peça para o usuário tentar descobrir 
# qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
print('-=-' * 20)
print('Vou pensar em um número 0 e 5. Tente adivinhar...')
print('-=-' * 20)

from random import randint
from time import sleep

computador = randint(0,5)

jogador = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3) #segundos

if jogador == computador:
    print('Prabens! você conseguiu me ganhar.')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))