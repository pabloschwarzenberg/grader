#Descomponer un número
import sys
numero=str(input("Ingrese un numero de hasta 4 digitos: "))

if len(numero)==4:
    a=numero[0]
    b=numero[1]
    c=numero[2]
    d=numero[3]
    print(a,"M+",b,"C+",c,"D+",d,"U")
    
elif len(numero)==3:
    a=numero[0]
    b=numero[1]
    c=numero[2]
    print(a,"C+",b,"D+",c,"U")
    
elif len(numero)==2:
    a=numero[0]
    b=numero[1]
    print(a,"D+",b,"U")
    
elif len(numero)==1:
    a=numero[0]
    print(a,"U")
else:
    print("numero no permitido")
    sys.exit(0)     