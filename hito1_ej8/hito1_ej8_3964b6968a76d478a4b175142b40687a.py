#Descomponer un número
d=int(input("ingresa un numero de 4 digitos: "))
if d>999:

 umil=d//1000
 sobrante=d%1000

 centenas=sobrante//100
 sobrante2=sobrante%100

 decenas=sobrante2//10
 unidades=sobrante%10

 print(umil,"M +",centenas,"C +",decenas,"D +",unidades,"U")
elif d>99:
    centenas=d//100
    sobrante=d%100

    decenas=sobrante//10
    unidades=sobrante%10

    print(centenas,"C +",decenas,"D +",unidades,"U")
elif d>9:
    decenas=d//10
    unidades=d%10
    print(decenas,"D +",unidades,"U")
elif d>0:
   print(d,"U")