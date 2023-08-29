#Descomponer un número
def imprimir_descarga(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10
    
    descarga = ""
    
    if miles > 0:
        descarga += str(miles) + "M "
    
    if centenas > 0:
        descarga += str(centenas) + "C "
    
    if decenas > 0:
        descarga += str(decenas) + "D "
    
    if unidades > 0:
        descarga += str(unidades) + "U "
    
    print("Descarga:", descarga)


# Solicitar número al usuario
numero = int(input("Ingresa un número de hasta 4 dígitos: "))
imprimir_descarga(numero)     