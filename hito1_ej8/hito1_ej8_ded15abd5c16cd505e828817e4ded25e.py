#Descomponer un número
n=(input("Ingresa un numero de hasta 4 digitos"))
largo=len(n)
i=0
if largo==4:
    print((n[0]),"M+",(n[1]),"C+",(n[2]),"D+",(n[3]),"U")
elif largo==3:
    print((n[0]),"C+",(n[1]),"D+",(n[2]),"U")
elif largo==2:
    print((n[0]),"D+",(n[1]),"U")
elif largo==1:
    print((n[0]),"U")      