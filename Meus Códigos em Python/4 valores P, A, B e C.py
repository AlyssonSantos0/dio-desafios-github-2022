P = float(input('Diga o 1º número: '))
A = float(input('Diga o 2º número: '))
B = float(input('Diga o 3º número: '))
C = float(input('Diga o 4º número: '))
if P==1:
    print('Sua média: {:.1f}'.format((A+B+C)/3))
elif P==2:
    som = A+B+C
    print(f'Soma dos 3 valores: {som}')
elif P==3:
    if B % 2:
        print(f'{B} é Par')
    else:
        print(f'{B} é Impar')
else:
    print('______OPERAÇÃO INVÁLIDA______')
