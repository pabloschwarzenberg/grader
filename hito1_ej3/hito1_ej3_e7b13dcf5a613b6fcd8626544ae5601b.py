#Aprobación de créditos
def credito(ingreso, anio, hijos, pertenencia, estado_civil, cc):
    rechazado = "RECHAZADO"
    aceptado = "APROBADO"
    if(pertenencia > 10 and hijos >= 2):
        return aceptado
    elif(estado_civil == "C" and hijos > 3 and anio-2018 >= 45 and anio-2018 <= 55):
        return aceptado
    elif(ingreso > 2500000 and estado_civil == "S" and cc == "U"):
        return aceptado
    elif(ingreso > 3500000 and pertenencia > 5):
        return aceptado
    elif(cc == "R" and estado_civil == "C" and hijos < 2):
        return aceptado
    else:
        return rechazado

ingreso = int(input("Ingresos: "))
anio = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Iingrese la cantidad de hijos que tiene: "))
pertenencia = int(input("Ingrese los años que lleva pertenenciendo al banco: "))
estado_civil = input("Ingrese su estado civil Soltero o Casado(S/C): ")
cc = input("Ingrese si vive en una zona Rural o Urbana(R/U): ")

resultado = credito(ingreso, anio, hijos, pertenencia, estado_civil, cc)
print(resultado)

