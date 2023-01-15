#Crie um programa que tenha uma tupla única com nomes de produtos
#  e seus respectivos preços, na sequência. No final,
#  mostre uma listagem de preços, organizando os dados em forma tabular.

# print("="*50)
# print("          LISTAGEM DE PREÇOS          ")
# print("="*50)

tupla_precos = ('Lápis..................................R$',    1.75,
                'Borracha...............................R$',    2.00,
                'Caderno................................R$',   15.90,
                'Estojo.................................R$',   25.00,
                'Transferidor...........................R$',   4.20,
                'Compasso...............................R$',   9.9,
                'Mochila................................R$',  120.32,
                'Canetas................................R$',   22.30,
                'Livro..................................R$',   34.90)
print("_"*50)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_'*50)

for x in range(0, len(tupla_precos)):
    if x % 2 == 0:
        print(f'{tupla_precos[x]:<30}', end='')
    else:
        print(f'R${tupla_precos[x]:>7.2f}')
print("_"*50)