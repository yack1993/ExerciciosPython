#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = int(input('Informe o número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num //100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidadade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))