#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Informe o ângulo que você deseja: '))

radiano = math.radians(angulo)
seno = math.sin(radiano)
cos = math.cos(radiano)
tang = math.tan(radiano)

print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(angulo,cos))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(angulo, tang))