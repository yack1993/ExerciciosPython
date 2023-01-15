# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a 
# letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite a Frase: ').strip().upper()
print('A letra A parece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A Ultima letra A apareceu na posição {}'.format(frase.rfind('A') + 1))
