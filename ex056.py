#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
quant_mulher = 0

for p in range(1,5):
    print("====== {}ª PESSOA =======".format(p))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

    soma_idade += idade

    if p == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_velho = nome

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo == 'F' and idade < 20:
        quant_mulher += 1


media_idade = soma_idade / 4
print('A média de idade é de {:.1f} anos '.format(media_idade))
print('O home mais velho tem {} anos e o chamam {}'.format(maior_idade_homem, nome_velho))
print("Ao todo é/são {} mulher/(mulheres) com menos de 20 anos".format(quant_mulher))
