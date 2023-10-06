## Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

SalárioHora = float(input('Quanto você ganha por hora? '))
HorasTrabalhadas = float(input('Quantas horas você trabalhou? '))
SalárioMês = SalárioHora * HorasTrabalhadas
print('O seu salário é R$ {}.'.format(SalárioMês))