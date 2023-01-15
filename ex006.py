#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
import math
n = int(input('Informe o número: '))
dobro = n * 2
triplo = n * 3
raiz = math.isqrt(n)
print('O dobro de {} é {}'.format(n,dobro))
print('O triplo de {} é {}'.format(n,triplo))
print('A raiz quadrada de {} é {:.2f}'.format(n, raiz))