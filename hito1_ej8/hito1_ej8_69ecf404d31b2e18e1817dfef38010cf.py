#Descomponer un número
numero = str(input("Ingresa tu numero: "))
M = 1000
C = 100
D = 10
U = 1
if len(numero)==4:
    print((numero[0]),"M+",(numero[1]),"C+",(numero[2]),"D+",(numero[3]),"U")
if len(numero)==3:
    print((numero[0]),"C+",(numero[1]),"D+",(numero[2]),"U")
if len(numero)==2:
    print((numero[0]),"D+",(numero[1]),"U")
if len(numero)==1:
    print(numero[0],"U")
    