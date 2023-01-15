# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = int(input("Informe o peso (Kg): "))
alt = float(input('Informe a altura (m): '))

imc = peso / (alt ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal')
elif imc <= 18.5 or imc < 25:
    print('PARABÉNS, você está na faixa de peso Normal.')
elif imc <= 25 or imc < 30:
    print('Você está na faixa Sobrepeso')
elif imc <= 30 or imc <= 40:
    print('Você está na faixa de Obesidade')
elif imc > 40:
    print('Você está na faixa de Obesidade Mórbida')