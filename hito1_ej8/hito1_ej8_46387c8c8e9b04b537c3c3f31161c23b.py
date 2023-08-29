#Descomponer un número
Numero = int(input("Inserte numero: "))
Numero = str(Numero)
x = len(Numero)
if x == 4:
    a = Numero[0]
    b = Numero[1]
    c = Numero[2]
    d = Numero[3]
    print(a,"M+",b,"C+",c,"D+",d,"U")
elif x == 3:
    a = Numero[0]
    b = Numero[1]
    c = Numero[2]
    print(a,"C+",b,"D+",c,"U")
elif x == 2:
    a = Numero[0]
    b = Numero[1]
    print(a,"D+",b,"U")
elif x == 1:
    a = Numero[0]
    print(a,"U")

