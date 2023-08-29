#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Rellenar con ceros si el número tiene menos de 4 dígitos
numero = numero.zfill(4)

descomposicion = ""

descomposicion += f"{numero[0]}M + "
descomposicion += f"{numero[1]}C + "
descomposicion += f"{numero[2]}D + "
descomposicion += f"{numero[3]}U"

# Eliminar los ceros iniciales
descomposicion = descomposicion.replace("0M + ", "")
descomposicion = descomposicion.replace("0C + ", "")
descomposicion = descomposicion.replace("0D + ", "")

print("Descomposición:", descomposicion)