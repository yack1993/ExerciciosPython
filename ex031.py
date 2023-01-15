#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
d = float(input('Informe a distaância da viagem: '))
print('Você está prestes a começar uma viagem de {:.1f}'.format(d))
if d <= 200:
    preco = d * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
else:
    preco = d * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))


