# Entrada
cadena = str(input("Ingrese cadena: "))

# Asignacion 
secuencia = ""
genoma = "ACTGactg"

# Proceso
for i in cadena:
    if i in genoma:
        secuencia += i
    else:
        print("La secuencia", cadena, "es incorrecta")

# Salida
print("La secuencia", secuencia, "es correcta")