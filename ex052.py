#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input("informe o número: "))
total =0
for c in range(1, n + 1):
    if n % c == 0:
        #print('\033[33m', end=' ')
        print(end=' ')
        total += 1
    else:
        #print('\033[31m', end=' ')
        print(end=' ')
    print('{}'.format(c), end='')
print('\nO número {} foi dívisivel {} vezez'.format(n, total))
if total == 2:
    print('{} é um número é Primo'.format(n))
else:
    print('{} não é um número Primo'.format(n))
    