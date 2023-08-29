#Suma de los N primeros números
while True:
    n=int(input("ingrese un numero dentro de los naturales: "))
    if(n>=0):
        resultado=n*(n+1)/2
        print(resultado)
        break

    else:
        print("EL numero ingresado no es valido")