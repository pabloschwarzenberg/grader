#Descomponer un número
V=str(input("Escriba un numero de hasta 4 cifras "))
N=len(V)
if N==4:
    x4=int(V[3])
    x3=int(V[2])
    x2=int(V[1])
    x1=int(V[0])
    print("El numero tiene:",x1,"M +",x2,"C +",x3,"D +",x4,"U")
elif N==3:
    x3=int(V[2])
    x2=int(V[1])
    x1=int(V[0])
    print("El numero tiene:",x1,"C +",x2,"D +",x3,"U")
elif N==2:
    x2 = int(V[1])
    x1 = int(V[0])
    print("El numero tiene:",x1,"D +",x2,"U")
elif N==1:
    x1 = int(V[0])
    print("El numero tiene:",x1,"U")

else:
    print("este programa descompone hasta un maximo de 4 cifras!!")