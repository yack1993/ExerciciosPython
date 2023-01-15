#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
v1 = int(input('Informe 1º valor: '))
v2 = int(input('Informe 2º valor: '))
v3 = int(input('Informe 3º valor: '))

maior = v1
menor = v1

#Maior
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

#Menor
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3



print('O maior valor digitado foi: {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))