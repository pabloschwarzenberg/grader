cadena = input("Ingrese cadena a comprobar: ")
n = int(input("Ingrese un numero: "))

def cadenaSeparada(cadena, n):
    resultado = ""
    if len(cadena) % n != 0:
        return "ninguna"
    else:
        for i in range(0, len(cadena), n):
            resultado += cadena[i:(i+n)] + " "
        return resultado

print(cadenaSeparada(cadena, n))