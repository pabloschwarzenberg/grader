numero = []

numero = input("Ingrese el numero")
suma = 0
i = 1

for n in reversed(numero):
    
    multiplicacion = int(float(n)) * i

    suma = suma + multiplicacion
    modulo = suma / 11
    resto = suma - (11 * int(modulo))
    resultado = 11 - resto

    if(i == 7):
        i = 1

    i += 1


if(resultado == 11):
    print("dv = 11")
elif(resultado == 10):
    print("dv = K")
else:
    print("dv=",resultado)