numero=int(input('ingrese un numero decimal'))
binario=''
while numero !=0:
    unocero= int(numero%2)
    numero= int(numero/2)
    binario= str(unocero)+ binario
print('resultado=',binario)