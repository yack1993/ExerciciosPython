#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valorCasa = float(input('Informe o valor da casa: '))
salComprador = float(input('Informe salário comprador: '))
anosFinanc = int(input('Informe quantos de financimanto: '))
prestacao = valorCasa / (anosFinanc * 12)
minimo = (salComprador * 30)/100

print('Para pagar a casa de R${} em {} anos a prestação será de R${}'.format(valorCasa, anosFinanc, prestacao))

if(prestacao <= minimo):
    print('Empréstimo pode ser concedido!')
else:
    print('Empréstimo não pode ser concedido!')