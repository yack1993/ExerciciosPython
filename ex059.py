#Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

# import time
from time import sleep

n1 = float(input('Informe 1º valor: '))
n2 = float(input('Informe 2º valor: '))
opcao = 0

while opcao != 5:
    print('''  
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair dp programa''')

    opcao = int(input('>>>>> Qual é a sua opção: '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
         mult = n1 * n2
         print('A soma entre {} + {} é {}'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior é: {}'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior é: {}'.format(n1, n2, maior))
        else:
            print('Números iguais')
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = float(input('Informe 1º valor: '))
        n2 = float(input('Informe 2º valor: '))

    else:
        print('Opção Invalida. Tente novamente')
    print('=->' * 10)
    sleep(2)
print('Fim do programa! Volte sempre')
