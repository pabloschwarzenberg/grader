#Cálculo del dígito verificador de un rut
def calcular_dv(rut):
    rut = rut[::-1]
    factor = 2
    suma = 0
    
    for digito in rut:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2
    
    dv = 11 - (suma % 11)
    if dv == 11:
        return "0"
    elif dv == 10:
        return "K"
    else:
        return str(dv)


rut_sin_formato = input("Ingrese el RUT sin puntos ni guiones: ")
dv = calcular_dv(rut_sin_formato)
print("dv=", dv)