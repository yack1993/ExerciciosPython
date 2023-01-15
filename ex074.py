#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint


count = 1
num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores sorteados foram: ', end='')
for n in num:
    print('{} '.format(n), end='')

print('\nO maior valor sorteado foi: {}'.format(max(num)))
print('O menor valor sorteado foi {}'.format(min(num)))
    