# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considerano dolar US$1 == R$3,27
valor = float(input('Informe o valor em R$: '))
dolar = valor / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(valor, dolar))