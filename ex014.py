#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
tempCelsius = float(input('Informe a temperatura em ºC: '))
tempFahrenheit = (tempCelsius * 1.8) + 32
tempFahrenheit2 = (tempCelsius * (9/5)) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF'.format(tempCelsius, tempFahrenheit2))