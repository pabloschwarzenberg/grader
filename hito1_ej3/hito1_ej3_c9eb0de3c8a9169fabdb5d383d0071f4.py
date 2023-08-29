def credito(I, AN, NH, AB, EC, CoC):
    if AN > 10 and NH >= 2:
        return "APROBADO"
    elif NH > 3 and EC == "C" and AN > 1968 and AN < 1078:
        return "APROBADO"
    elif I > 2500000 and EC == "S" and CoC == "U":
        return "APROBADO"
    elif I > 3500000 and AB > 5:
        return "APROBADO"
    elif CoC == "R" and EC == "C" and NH < 2:
        return "APROBADO"
    else:
        return "RECHAZADO"

I = int(input("Ingreso: "))
AN = int(input("Año nacimiento: "))
NH = int(input("Número hijos: "))
AB = int(input("Años pertenencia al banco: "))
EC = input("Estado civil: ")
CoC = input("Campo o ciudad: ")

resultado = credito(I, AN, NH, AB, EC, CoC)
print(resultado)