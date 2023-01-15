#O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
alun1 = input('Informe 1º aluno: ')
alun2 = input('Informe 2º aluno: ')
alun3 = input('Informe 3º aluno: ')
alun4 = input('Informe 4º aluno: ')

lista = [alun1, alun2, alun3, alun4]
shuffle(lista)

print('A ordem de apresentação será: \n {}'.format(lista))