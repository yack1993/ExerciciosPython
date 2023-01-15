# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

print('-=-=-=-=-=-=-=-=-=-=-=-= LOJAS BIMA -=-=-=-=-=-=-=-=-=-=')

preco = float(input('Informe o preço: '))
print(''' Formas Pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ]  2x no cartão
[ 4 ] 3x ou mais no cartão
''')

opcao = int(input('Qual opção: '))

if opcao == 1:
    novo = preco - ((preco * 10) / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(preco, novo))
elif opcao == 2:
    novo = preco - ((preco * 5) / 100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(preco, novo))
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))
    print('Sua compra de R${} vai custar R${} no final!'.format(preco, total))
elif opcao == 4:
    total  = preco + (preco * 20) / 100
    totalparc = int(input('Quantas parcelas: '))
    parc = total / totalparc
    
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(totalparc, parc))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(preco, total))
else:
    print('Opção inválida. Tente novamente')
