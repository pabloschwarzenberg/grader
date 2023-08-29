#Descomponer un número
def imprimir_descarga(numero):
    # Convertir el número a cadena y completar con ceros a la izquierda si tiene menos de 4 dígitos
    numero_str = str(numero).zfill(4)
    
    # Obtener los dígitos individuales
    miles = int(numero_str[0])
    centenas = int(numero_str[1])
    decenas = int(numero_str[2])
    unidades = int(numero_str[3])
    
    # Imprimir la descarga en el formato solicitado
    descarga = ""
    if miles > 0:
        descarga += str(miles) + "M + "
    if centenas > 0:
        descarga += str(centenas) + "C + "
    if decenas > 0:
        descarga += str(decenas) + "D + "
    descarga += str(unidades) + "U"
    
    print(descarga)


# Ejemplo de uso
numero = int(input("Ingresa un número de hasta 4 dígitos: "))
imprimir_descarga(numero)      