#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO
n1 = float(input('Informe 1ª nota: '))
n2 = float(input('Informe 2ª nota: '))

media = (n1 + n2) / 2

if media < 5 :
    print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, media))
    print('O aluno está  REPROVADO')
elif media >= 5 and media <= 6.9:
    print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, media))
    print('O aluno está RECUPERAÇÃO')
elif media > 7:
    print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, media))
    print('O aluno está APROVADO')