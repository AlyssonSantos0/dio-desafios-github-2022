cartao= int( input('Digite o número do seu cartão: '))
lim= float ( input('Limite Disponível para Compra: R$ '))
com= float ( input('Qual o valor da compra: R$ '))
if com>lim:
    print ('Sua Compra Excede seu Limite')
    print ('Obrigado Não Foi Possível Completa a Operação')
elif com<=lim:
    par= int ( input('Parcelas: '))
dis= lim-com
val= com/par
pagbank= 4350870095413849
crefisa= 5133546642148788
superget= 6504120004605469
magazineluiza= 5309940588800569
inter= 5117810364373366
if cartao==4350870095413849 or cartao==5133546642148788 or cartao==6504120004605469 or cartao==5309940588800569 or cartao==5117810364373366:
    print (f'Valor das Parcelas: R${val}')
    print (f'Limite Restante: R${dis}')
    print ('Compra Realizada com Sucesso.')
elif cartao!=4350870095413849 or cartao!=5133546642148788 or cartao!=6504120004605469 or cartao!=5309940588800569 or cartao!=5117810364373366:
      print ('Compra não Autorizada.')