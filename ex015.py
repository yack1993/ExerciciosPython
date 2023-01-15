#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

diasAlugados = int(input('Informe os dias alugados: '))
kmRodados = int(input('Informe KM  rodados: '))
total = (kmRodados * 0.15) + (diasAlugados * 60)
print('Total a pagar é de R${:.2f}'.format(total))