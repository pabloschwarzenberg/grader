numero=int(input("Ingrese un numero de hasta 4 digitos: "))
numstr=str(numero)
l=len(numstr)
if l==4:
    miles= (numero//1000)
    centenas= (numero//100)%10
    decenas= (numero%100)//10
    unidades= (numero%10)
    print("{}M+{}C+{}D+{}U".format(miles,centenas,decenas,unidades))
if l==3:
    unidades= (numero%100)%10
    decenas= (numero%100)//10
    centenas= (numero%1000)//100
    print("{}C+{}D+{}U".format(centenas,decenas,unidades))
if l==2:
    decenas= (numero//10)
    unidades= (numero%10)
    print("{}D+{}U".format(decenas, unidades))
if l==1:
    unidades=numero
    print("{}U".format(unidades))