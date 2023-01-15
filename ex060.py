#Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('Informe seu número para calcular seu Fatorial: '))
c = n
result = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    result *= c
    c -= 1
print('{}'.format(result))