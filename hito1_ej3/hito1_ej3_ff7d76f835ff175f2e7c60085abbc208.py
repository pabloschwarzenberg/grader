#Aprobación de créditos

ingreso = eval(input("¿Cúal es su ingreso? >>> "))
nacimiento = eval(input("¿En qué año nació? >>> "))
hijos = eval(input("¿Cuántos hijos tiene? >>> "))
convenio = eval(input("¿Cuántos años lleva con nocostros? >>> "))
estadoCivil = str(input("¿Soltero(S) o casado(C)? >>> "))
vivienda = str(input("¿Vive en campo(R) o ciudad(U)? >>> "))

edad = 2020 - nacimiento

if convenio >= 10 and hijos >= 2:
    print("APROBADO")
elif estadoCivil == "C" and hijos >= 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso >= 250000 and estadoCivil == "S" and vivienda == "U":
    print("APROBADO")
elif ingreso >= 350000 and convenio >= 5:
    print("APROBADO")
elif vivienda == "U" and estadoCivil == "C" and hijos <= 1:
    print("APROBADO")
else:
    print("RECHAZO")
