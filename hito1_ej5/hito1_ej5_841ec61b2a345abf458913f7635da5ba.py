def calculaverificador(rut):
    rut = str(rut)  

    if not rut.isdigit() or len(rut) < 1:
        return "RUT inválido"

    rutreverso = rut[::-1]   
    factor = 2
    suma = 0

    for digito in rutreverso:
        suma += int(digito) * factor
        factor += 1
        if factor > 7:
            factor = 2

    dverificador = 11 - (suma % 11)
    if dverificador == 11:
        dverificador = "0"
    elif dverificador == 10:
        dverificador = "K"

    return dverificador


rutingresa = input("Ingrese el número de RUT sin el dígito verificador: ")

dicalculado = calculaverificador(rutingresa)
print("dv=", dicalculado)