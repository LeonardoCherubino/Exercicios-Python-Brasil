
## Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

Base = int(input('Entre com a base do quadrado em metros. '))
Altura = int(input('Entre com a altura do quadrado em metros. '))
Área = Base * Altura
print('A área desse quadrado é {}m² e o dobro dessa área é {}m².'.format(Área, Área * 2))

QuantidadeDeLitrosDeTinta = Área / 3
print('Você vai precisar de {} litros de tinta. '.format(QuantidadeDeLitrosDeTinta))
QuantidadeDeLatasDeTinta = QuantidadeDeLitrosDeTinta / 18
print('Você vai precisar de {} latas de tinta. '.format(QuantidadeDeLatasDeTinta))
Preço = QuantidadeDeLatasDeTinta * 80
print('O preço é {}. '.format(Preço))