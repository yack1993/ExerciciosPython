#Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 

print("="*20)
print("CADASTRA UMA PESSOA")
print("="*20)

count18=0
countH = 0
countM20 = 0

while True:
    idade = int(input('Informe a Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Informe o Sexo [M/F]: ').strip().upper()
    if idade >=18:
        count18 += 1
    if sexo == 'M':
        countH += 1
    if sexo == 'F' and idade < 20:
        countM20 += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = input("Quer continuar? [S/N] ").strip().upper()
    if opcao == 'N':
        break
        
print('Tem {} pessoas com mais de 18 anos!'.format(count18))
print('Foram cadastrados {} homens!'.format(countH))
print('Tem {} mulheres cadastradas com menos de 20 anos'.format(countM20))





