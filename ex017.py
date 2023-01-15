#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
catOposto = float(input('Comprimento do cateto oposto: '))
catAdjacente = float(input('Comprimento do cateto adjacente: '))

#hi = ((catOposto ** 2) + (catAdjacente ** 2)) ** (1/2) #raiz quadrada
hi1 = hypot(catOposto, catAdjacente)

print('A hipotenusa vai medir {:.2f}'.format(hi1))