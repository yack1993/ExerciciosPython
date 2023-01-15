#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = input('Qual cidade você nasceu? ').strip().upper()
c = cidade.split()
print(c[0] == 'SANTO')
