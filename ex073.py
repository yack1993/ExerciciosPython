#Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.

times = ('Corinthinas', 'Flamengo', 'São Paulo', 'Palmeiras', 'Atletico Mineiro','Chapecoense', 'Fluminense', 'Cruzeiro', 
'Gremio', 'Santos', 'Vasco', 'Botafogo', 'Curitiba')


print('-='*30)
print('Lista de times do Brasileirão: {}'.format(times))
print('-='*30)

print('-='*30)
print('Os 5 primeiros são: {}'.format(times[0:5]))
print('-='*30)

print('-='*30)
print('Os últimos 4 são: {}'.format(times[-4:]))
print('-='*30)

print('-='*30)
print('Times em ordem alfabética: {}'.format(sorted(times)))
print('-='*30)

print('-='*30)
print('O time da Chapecoense está na {}ª posição '.format(times.index('Chapecoense')+1))
print('-='*30)

