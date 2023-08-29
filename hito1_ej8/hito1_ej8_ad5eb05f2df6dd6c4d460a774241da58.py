#Descomponer un número
numero=int(input("ingrese un numero de hasta 4 digitos: "))
unidad=numero%10
numero=int((numero-unidad)/10)
decena=numero%10
numero=int((numero-decena)/10)
centena=numero%10
numero=int((numero-centena)/10)
miles=numero
if decena==0 and centena==0 and miles==0:
    print(unidad,"U")
elif centena==0 and miles==0:
    print(decena,"D +",unidad,"U")
elif miles==0:
    print(centena,"C +",decena,"D +",unidad,"U")
else:
    print(miles,"M +",centena,"C +",decena,"D +",unidad,"U")            
        
      