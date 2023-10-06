## Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
## Para homens: (72.7*h) - 58
## Para mulheres: (62.1*h) - 44.7

Altura = float(input('Qual é a sua altura? '))
PesoIdealHomem = (72.7 * Altura) - 58
PesoIdealMulher = (62.1 * Altura) - 44.7
print('Se você é homem seu peso ideal é {} quilos. '.format(PesoIdealHomem))
print('Se você é mulher seu peso ideal é {} quilos. '.format(PesoIdealMulher))