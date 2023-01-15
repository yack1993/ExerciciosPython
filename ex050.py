# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# n1 = int(input('Informe número1: '))
# n2 = int(input('Informe número2: '))
# n3 = int(input('Informe número3: '))
# n4 = int(input('Informe número4: '))
soma=0
count = 0
for n in range(1,5):
    num = int(input("Informe o {}º valor: ".format(n)))
    if num % 2 == 0:
        soma += num
        count = count + 1
        print(count)
    else:
        pass
print('Você informou {} pares e a soma dos números pares é: {}'.format(count, soma))