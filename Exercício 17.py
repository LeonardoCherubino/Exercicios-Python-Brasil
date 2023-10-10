## Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros ## ## quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
## Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
## comprar apenas latas de 18 litros;
## comprar apenas galões de 3,6 litros;
## misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

Base = float(input('Entre com a base do quadrado em metros. '))
Altura = float(input('Entre com a altura do quadrado em metros. '))
Área = Base * Altura
print('A área a ser pintada é {}m²'.format(Área))
QuantidadeDeLitrosDeTinta = Área / 6
print('Você vai precisar de {} litros de tinta pra pintar {}m².'.format(QuantidadeDeLitrosDeTinta, Área))
QuantidadeDeLatasDeTintaGrande = QuantidadeDeLitrosDeTinta / 18
QuantidadeDeLatasDeTintaPequeno = QuantidadeDeLitrosDeTinta / 3.6
PreçoLataDeTintaGrande = QuantidadeDeLatasDeTintaGrande * 80
PreçoLataDeTintaPequeno = QuantidadeDeLatasDeTintaPequeno * 25

print('Você vai precisar de {} latas de tinta de 18 litros a custo de R$ {}.'.format(QuantidadeDeLatasDeTintaGrande, PreçoLataDeTintaGrande))
print('Você vai precisar de {} latas de tinta de 3,6 litros a um custo de R$ {}. '.format(QuantidadeDeLatasDeTintaPequeno, PreçoLataDeTintaPequeno))

if QuantidadeDeLatasDeTintaGrande <= 18:
    QuantidadeDeLatasDeTintaGrande = 1
print(QuantidadeDeLatasDeTintaGrande)
    
    