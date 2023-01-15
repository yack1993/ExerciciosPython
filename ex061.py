#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, 
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print("GERANDO PA")
print("=" * 20)

prim = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = prim
count = 1

# decimo = prim + (10-1) * razao
# print(decimo)

while count <=10:
    print('{} -> '.format(termo), end='')
    termo += prim
    count +=1
print('Fim')

 