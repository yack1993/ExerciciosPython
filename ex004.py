# Faça um programa que leia algo pelo teclado e mostre na tela o seu 
# tipo primitivo e todas as informações possíveis sobre ele.
valor = input('Digite algo: ')
print('O tipo primitivo desse valor é: {}'.format(type(valor)))
print('Só tem espaços: {}'.format(valor.isspace()))
print('É númerico: {}'.format(valor.isnumeric()))
print('É alfabetico: {}'.format(valor.isalpha()))
print('É alfanumerico: {}'.format(valor.isalnum()))
print('Está em Maiúscula: {}'.format(valor.isupper()))
print('Está em minúscula: {}'.format(valor.islower()))
print('Está capitalizada: {}'.format(valor.istitle()))
