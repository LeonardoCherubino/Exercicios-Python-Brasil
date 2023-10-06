## Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
## C = 5 * ((F-32) / 9)

Fahrenheit = float(input('Entre com a temperatura em graus Fahrenheit. '))
Celsius = 5 * ((Fahrenheit - 32) / 9)
print('{}° Fahrenheit correspodem a {}° Celsius. '.format(Fahrenheit, Celsius))

