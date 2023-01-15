#Desenvolva um programa que leia o primeiro termo e a razão de uma PA(Progressão aritimetica). 
# No final, mostre os 10 primeiros termos dessa progressão.
print("=" * 20)
print("10 TERMOS DE UMA PA")
print("=" *20)

prim = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

decimo = prim + (10-1) * razao

#prim=0,razao=2
#prim=25,razao=5


for c in range(prim, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('Acabou!')