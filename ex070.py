#Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 

somaCompra = 0
produto1000 = 0
listaPreco = []
barato = ''
while True:
    prod = input('Informe o produto: ').title()
    preco = float(input('Informe o preço: '))

    somaCompra = somaCompra + preco

    listaPreco.append(preco)
    maisBarato = min(listaPreco)

    if maisBarato == preco:
        barato = prod

    if preco > 1000:
       produto1000 += 1
    


    opcao = ' '
    while opcao not in 'SN':
        opcao = input("Quer continuar [S/N] ").strip().upper()
    if opcao == 'N':
        break

print('Total gasto na compra é de R${:.2f}'.format(somaCompra))
print('Temos {} produtos que custa mais de R$1000.00'.format(produto1000))
print('O produto mais barato foi {} e custa R${:.2f}'.format(barato, maisBarato))