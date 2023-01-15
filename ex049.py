#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Informe o número: '))
for c in range(1,11):
    print('{} x {} = {}'.format(num, c, num * c))