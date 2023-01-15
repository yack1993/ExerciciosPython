#Crie um programa que simule o funcionamento de um caixa eletrônico. 
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o 
# programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print("="*30)
print(" BANCO NOVO ")
print("="*30)

valor = int(input('Informe o valor: '))
total = valor
cedula = 50
total_cedula = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print('Total de {} cédulas de R${}'.format(total_cedula, cedula))
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if total == 0:
            break
print('='*30)

print("Volte sempre ao BANCO NOVO! Tenha um bom dia.")