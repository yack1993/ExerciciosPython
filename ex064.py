#Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, 
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n1 = int(input('Digite um número [999 para parar]: '))
count = 0
soma = 0
while n1 != 999:
    soma = soma + n1
    count +=1
    n1 = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles é de {}'.format(count, soma))