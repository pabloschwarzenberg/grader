#Cálculo del dígito verificador de un rut
      def calcular_digito_verificador(rut):
    rut = str(rut)
    reverso = rut[::-1]
    multiplicador = 2
    suma = 0

    for digito in reverso:
        suma += int(digito) * multiplicador
        multiplicador += 1
        if multiplicador > 7:
            multiplicador = 2

    resto = suma % 11
    dv = 11 - resto
    if dv == 10:
        return "k"
    elif dv == 11:
        return "0"
    else:
        return str(dv)

rut = int(input("Ingrese el número de rut: "))

dv = calcular_digito_verificador(rut)

print("dv=" + dv)