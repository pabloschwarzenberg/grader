N= int(input("Ingrese un número natural: "))
suma_naturales= N*(N+1)/2

if (N<0):
    print("El número ingresado no es un número natural")
else:
    if(suma_naturales>=0):
        suma= N*(N+1)/2
        print("La suma de los N primeros números naturales es: ", suma)