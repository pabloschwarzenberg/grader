#Cálculo del dígito verificador de un rut

Rut= int(input("Ingrese rut: "))

def dv(rut):
    serie= 2
    suma= 0
    contador= 0
    rutstr= str (rut)
    for digito in reversed (rutstr):
        suma= suma+ (int (digito) * serie)
        serie= serie + 1
        if serie == 8:
            serie = 2

    modulo= suma//11

    resto_division_entera= suma-(11*modulo)

    resto_total= 11-resto_division_entera

    if resto_total==11: return print ("dv=0")
    elif resto_total==10: return print ("dv=k")
    else: return print ("dv=", resto_total)

dv(Rut)