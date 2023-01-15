# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

r1 = int(input('1º segmento: '))
r2 = int(input('2º segmento: '))
r3= int(input('3º segmento: '))

if r1 < (r2 + r3) or r2 < (r1 + r3) or r3 < (r1 + r2):
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO ')
    else:
        print('ISÓSCELES')

else:
    print('Os segmentos  acima não podem formar um triângulo {}')
