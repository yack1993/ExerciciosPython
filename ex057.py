
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#  Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Infome o sexo [M/F]: ').strip().upper()

# if sexo == 'M':
#     print('Sexo {} regristado com sucesso!'.format(sexo))
# elif sexo == 'F':
#      print('Sexo {} regristado com sucesso!'.format(sexo))
# else:
#     print('Dados inválidos')

while sexo not in('M', 'F'):
    sexo = input('Dados inválidos. Por favor, informe seu sexo: ').strip().upper()
print('Sexo {} regristado com sucesso!'.format(sexo))


