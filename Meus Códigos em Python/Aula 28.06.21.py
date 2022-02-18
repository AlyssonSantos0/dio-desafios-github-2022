numero1 = int(input('Informe 1º valor: '))
numero2 = int(input('Informe 2º valor: '))
if numero1 > 10:
    numero2 = numero2 + numero2 * 2
elif numero1 > 12:
    numero2 = numero2 + numero1 / 2 + 4 / 2
elif numero1 < 20:
    numero2 = numero2 + numero2 * 3 / 2
else:
    numero2 = 0
print(numero2)