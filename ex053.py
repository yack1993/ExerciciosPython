#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Informe a frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso_novo = junto[::-1]
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
print('O inverso de {} é {}!'.format(junto, inverso_novo))

if inverso_novo == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')