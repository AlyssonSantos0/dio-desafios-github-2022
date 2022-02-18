num = int( input('Diga um número: '))
num1 = int( input('Diga outro número: '))
num2 = int( input('Diga mais outro número: '))
if num>num1>num2:
    print('Em ordem crescente: ',num,',',num1,',',num2)
elif num2>num1>num:
    print('Em ordem crescente: ',num2,',',num1,',',num)
elif num1>num>num2:
    print('Em ordem crescente: ',num1,',',num,',',num2)
elif num1>num2>num:
    print('Em ordem crescente: ', num1, ',', num2, ',', num)
elif num2>num>num1:
    print('Em ordem crescente: ', num2, ',', num, ',', num1)