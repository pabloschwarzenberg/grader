#Aprobación de créditos
ing = int(input("ingresos (pesos): "))
aNac = int(input("año de nacimiento: "))
nHijos = int(input("numero de hijos: "))
aPert = int(input("años de pertenencia al banco: "))
eCivil = input("estado civil(soltero/casado): ")
dVive = input("vive en area (rural/urbana): ")

soltero = "s"
casado = "c"
rural = "r"
urbano = "u"

if aPert > 10 and nHijos >= 2:
    print("credito aprobado")
elif eCivil == casado and nHijos > 3 and 45 < (2020 - aNac) < 55:
    print("credito aprobado")
elif ing > 2500000 and eCivil == soltero and dVive == urbano:
    print("credito aprovado")
elif ing > 3500000 and aPert > 5:
    print("credito aprovado")
elif dVive == rural and eCivil == casado and nHijos < 2:
     print("credito aprovado")
else:
    print("credito rechazado")