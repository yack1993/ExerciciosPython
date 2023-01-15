# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" 
# em um número entre 0 e 10. Só que agora o jogador vai 
# tentar adivinhar até acertar, mostrando no final 
# quantos palpites foram necessários para vencer.

# import random
from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi?')

computador = randint(0,10)
# print(computador)

acertou = False
count = 0

while not acertou:
    jogador = int(input('Informme o seu palpite: '))
    count += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou com {} tentativas. Prabéns!'.format(count))
