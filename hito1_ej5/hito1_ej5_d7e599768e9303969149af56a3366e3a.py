#Cálculo del dígito verificador de un rut
def calcular_digito_verificador(rut):
    rut = str(rut)  # Convertir el RUT a cadena de caracteres
    rut = rut.replace(".", "")  # Remover puntos (si existen)
    rut = rut.replace("-", "")  # Remover guión (si existe)
    
    # Calcular el dígito verificador
    suma = 0
    multiplicador = 2
    
    # Recorrer el RUT en orden inverso
    for i in reversed(range(len(rut))):
        suma += int(rut[i]) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2
    
    # Calcular el dígito verificador como el complemento a 11 del resultado de la suma
    dv = 11 - (suma % 11)
    
    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = "k"
    
    return dv

# Solicitar al usuario que ingrese el RUT
rut = input("Ingrese el RUT sin dígito verificador: ")

# Calcular el dígito verificador
dv = calcular_digito_verificador(rut)

# Imprimir el resultado
print("dv =", dv)
      