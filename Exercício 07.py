## Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

Base = int(input('Entre com a base do quadrado em metros. '))
Altura = int(input('Entre com a altura do quadrado em metros. '))
Área = Base * Altura
print('A área desse quadrado é {}m² e o dobro dessa área é {}m².'.format(Área, Área * 2))