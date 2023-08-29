#Descomponer un número
numero=int(input("Ingrese un numero de hasta 4 digitos:"))
descomposicion=str(numero)

n=len(descomposicion)
#me da la cantidad de digitos del string

M="M"
C="C"
D="D"
U="U"

if n==4:
    miles=(descomposicion[0])
    centenas=(descomposicion[1])
    decenas=(descomposicion[2])
    unidades=(descomposicion[3])
    print(miles+M,"+",centenas+C,"+",decenas+D,"+",unidades+U)
elif n==3:
    centenas=(descomposicion[0])
    decenas=(descomposicion[1])
    unidades=(descomposicion[2])
    print(centenas+C,"+",decenas+D,"+",unidades+U)
elif n==2:
    decenas=(descomposicion[0])
    unidades=(descomposicion[1])
    print(decenas+D,"+",unidades+U)
elif n==1:
    unidades=(descomposicion[0])
    print(unidades+U)