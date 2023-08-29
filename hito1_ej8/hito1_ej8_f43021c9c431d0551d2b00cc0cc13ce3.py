print("Escriba un numero de hasta cuatro dígitos para obetener su descomposición en unidades, decenas, centenas y miles")
numero=input("Número: ")
if int(len(numero))==1:
     u=str(numero[0])
     print(u,"U")
elif int(len(numero))==2:
     d=str(numero[0])
     u=str(numero[1])
     print(d,"D + ",u,"U")
elif int(len(numero))==3:
     c=str(numero[0])
     d=str(numero[1])
     u=str(numero[2])
     print(c,"C + ",d,"D + ",u,"U")
elif len(numero)==4:
     m=numero[0]
     c=numero[1]
     d=numero[2]
     u=numero[3]
     print(m,"M + ",c,"C + ",d,"D + ",u,"U")
else:
     print("Compruebe el largo del número")
input("Presione cualquier tecla para terminar el programa")
