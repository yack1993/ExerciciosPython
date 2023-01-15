#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
n = input('Informe seu nome completo: ').strip()

nome = n.split()
count = len(nome) - 1

primeiro_nome = nome[0]
ultimo_nome = nome[count]

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(primeiro_nome))
print('Seu último nome é {}'.format(ultimo_nome))
print('Ultomo nome é {}'.format(nome[len(nome)-1]))