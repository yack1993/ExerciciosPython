#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
medida = float(input('Informe uma distância em metros: '))
kilometro=(medida/1000)
hectometro = (medida/100)
decametro=(medida/10)
decimetro=(medida*10)
centimetro = medida * 100
milimetro = medida * 1000




print('A medida de {} metros corresponde a \n {}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(medida,kilometro, hectometro, decametro, decimetro, centimetro, milimetro))
