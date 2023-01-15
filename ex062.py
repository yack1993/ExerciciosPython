#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#  O programa encerrará quando ele disser que quer mostrar 0 termos.
print("GERANDO PA")
print("=" * 20)

prim = int(input('Informe o 1º termo: '))
razao = int(input('Informe a razão: '))

termo = prim
count = 1
total = 0
mais = 10

while mais !=0:
    total = total + mais
    while count <= total:
        print('{} -> '.format(termo), end='')
        termo  += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostar a mais?'))
print('FIM')

 