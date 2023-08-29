#Descomponer un número
def descomponer_numero(numero):
    # Obtener los dígitos individuales
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10
    
    # Imprimir la descomposición
    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M "
    if centenas > 0:
        descomposicion += str(centenas) + "C "
    if decenas > 0:
        descomposicion += str(decenas) + "D "
    if unidades > 0:
        descomposicion += str(unidades) + "U "
    
    return descomposicion.strip()

# Pedir al usuario ingresar un número
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Obtener y mostrar la descomposición
descomposicion = descomponer_numero(numero)
print(descomposicion)
      