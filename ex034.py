# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salariofunc = float(input('Informe o salário do funcionário: '))
if salariofunc > 1250.00:
    aumento = salariofunc + ((salariofunc * 10) /100)
else:
    aumento = salariofunc + ((salariofunc * 15)/100)

print('Quem ganahava R${} passa a ganhar R${:.2f} agora'.format(salariofunc, aumento))