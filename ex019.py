#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, 
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
aluno1 = input('Informe 1º aluno: ')
aluno2 = input('Informe 2º aluno: ')
aluno3 = input('Informe 3º aluno: ')
aluno4 = input('Informe 4º aluno: ')

listaAlunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = choice(listaAlunos)

print('O aluno escolhido foi {}'.format(sorteado))