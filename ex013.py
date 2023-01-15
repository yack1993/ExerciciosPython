#Faça  um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Salário do funcionário R$: '))
aumento_salario = (salario * 15) / 100
novo_salario = salario + aumento_salario
print('O funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo_salario))