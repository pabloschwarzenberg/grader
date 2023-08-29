#Descomponer un número
q=int(input("ingresa un numero de 4 digitos: "))
if q>999:

 umil=q//1000
 sobrante=q%1000

 centenas=sobrante//100
 sobrante2=sobrante%100

 decenas=sobrante2//10
 unidades=sobrante%10

 print(umil,"M +",centenas,"C +",decenas,"D +",unidades,"U")
elif q>99:
    centenas=q//100
    sobrante=q%100

    decenas=sobrante//10
    unidades=sobrante%10

    print(centenas,"C +",decenas,"D +",unidades,"U")
elif q>9:
    decenas=q//10
    unidades=q%10
    print(decenas,"D +",unidades,"U")
elif q>0:
   print(q,"U")      