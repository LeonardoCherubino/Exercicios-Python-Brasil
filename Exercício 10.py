## Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
## F = ((9 x C) / 5) + 32

Celsius = float(input('Qual é a temperatura em graus Celsius? '))
Fahrenheit = ((9 * Celsius) / 5) + 32
print('{}º Celsius correspondem a {}° Fahrenheit. '.format(Celsius, Fahrenheit))


