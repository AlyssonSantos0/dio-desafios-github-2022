lista_idades = []
maior_idade = 0
menor_idade = 0

for i in range (0, 12):
    lista_idades.append(int(input('Digite uma idade: ')))
    if i == 0:
        maior_idade = menor_idade = lista_idades[i]
    else:
        if lista_idades[i] > maior_idade:
            maior_idade = lista_idades[i]
        if lista_idades[i] < menor_idade:
            menor_idade = lista_idades[i]

print('=-' * 25)
print('A maior idade recebida foi {}!'.format(maior_idade))
print('A menor idade recebida foi {}!'.format(menor_idade))