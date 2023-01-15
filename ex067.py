#Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

# n = int(input('Quer ver a tabuada de qual valor: '))


n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print('='*20)
    for valor in range(1,13):
        print('{} X {} = {}'.format(n, valor, n*valor))
    print('='*20)
    if n < 0:
        break
print('Programa tabuada encerrado. Volte sempre!')

