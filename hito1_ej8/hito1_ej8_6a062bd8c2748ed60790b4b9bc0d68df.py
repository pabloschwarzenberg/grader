numero = input("Ingrese un número de hasta 4 dígitos: ")

# Verificar que se haya ingresado un número válido de hasta 4 dígitos
if not numero.isdigit() or len(numero) > 4:
    print("Error: Debe ingresar un número válido de hasta 4 dígitos.")
    exit()

# Convertir el número a entero
numero = int(numero)

# Obtener los dígitos individuales
unidades = numero % 10
decenas = (numero // 10) % 10
centenas = (numero // 100) % 10
miles = (numero // 1000) % 10

# Crear una lista para almacenar los términos de la descomposición
terminos = []

# Agregar los términos con sus respectivos signos
if miles > 0:
    terminos.append(str(miles) + "M")
if centenas > 0:
    terminos.append(str(centenas) + "C")
if decenas > 0:
    terminos.append(str(decenas) + "D")
if unidades > 0:
    terminos.append(str(unidades) + "U")

# Imprimir la descomposición con los signos de suma
descomposicion = " + ".join(terminos)
print("Descomposición:", descomposicion)



