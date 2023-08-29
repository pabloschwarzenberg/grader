rut = input("Ingrese el número de RUT (sin dígito verificador): ")

# Verificar que el RUT sea válido
if not rut.isdigit() or len(rut) < 1:
    print("RUT inválido")
else:
    # Calcular el dígito verificador
    suma = 0
    multiplicador = 2
    for i in range(len(rut)-1, -1, -1):
        suma += int(rut[i]) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2
    
    resto = suma % 11
    dv = 11 - resto
    
    # Manejar casos especiales
    if dv == 11:
        dv = "0"
    elif dv == 10:
        dv = "K"
    else:
        dv = str(dv)
    
    print("dv=" + dv)
