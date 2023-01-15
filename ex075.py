#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n1 = int(input('Informe o 1º número:'))
n2 = int(input('Informe o 2º número:'))
n3 = int(input('Informe o 3º número:'))
n4 = int(input('Informe o 4º número:'))

tupla = (n1, n2, n3, n4)

print('Você digitou os valores {}'.format(tupla))
print('O valor 9 aparece {} vezes'.format(tupla.count(9)))
if 3 in tupla:

    print('O Valor 3 apareceu na {}ª posição'.format(tupla.index(3)+1))
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
