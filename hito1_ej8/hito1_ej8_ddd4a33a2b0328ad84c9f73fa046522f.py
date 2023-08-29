#Descomponer un número
numero=int(input("Ingrese un numero de hasta 4 digitos: "))
while not(numero<9999 and numero>0):
    N=int(input("Ingrese un numero de hasta 4 digitos: "))
largo=len(str(numero))
if largo==4:
    X1=str(numero)[0]
    X2=str(numero)[1]
    X3=str(numero)[2]
    X4=str(numero)[3]
    print( X1,"M+", X2,"C+", X3,"D+", X4,"U",)
if largo==3:
    X1=str(numero)[0]
    X2=str(numero)[1]
    X3=str(numero)[2]
    print( X1,"C+", X2,"D+", X3,"U",)
if largo==2:
    X1=str(numero)[0]
    X2=str(numero)[1]
    print( X1,"D+", X2,"U",)
if largo==1:
    X1=str(numero)[0]
    print(X1,"U",)