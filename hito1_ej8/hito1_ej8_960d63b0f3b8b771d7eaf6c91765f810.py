def descomponer_numero(numero):
    if numero < 0 or numero > 9999:
        return "El número debe estar entre 0 y 9999."
    
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = numero // 1000
    
    descomposicion = ""
    if miles > 0:
        descomposicion += str(miles) + "M "
    if centenas > 0:
        descomposicion += str(centenas) + "C "
    if decenas > 0:
        descomposicion += str(decenas) + "D "
    if unidades > 0:
        descomposicion += str(unidades) + "U"
    
    return descomposicion

# Ejemplo de uso
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

resultado = descomponer_numero(numero)
print(resultado)

      