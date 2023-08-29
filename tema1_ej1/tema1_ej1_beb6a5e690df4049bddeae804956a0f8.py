#Suma de los N primeros números
def sumadelosnaturales(A):
    sumanatural = 0
    for i in range(1, A + 1):
        sumanatural += i
    return sumanatural
#se define la suma, se coloca el for in para que funcione con el return hasta que no cumpla
B = int(input("Ingrese el valor de N: "))
#se pregunta el numero entero para hacer el calculo
resultadofinal = sumadelosnaturales(B)
print("La suma de los", B, "primeros números naturales es:", resultadofinal)
#se imprimen los resultados