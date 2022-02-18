lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

lista_im=[]
lista_par=[]
print(f'lista e {lista}')

for c in lista:
    if c % 2 ==0:
        lista_par.append(c)
    else:
        lista_im.append(c)

print(f'sua lista de numeros impar é{lista_im}')
print(f'sua lista de numeros pares é {lista_par}')