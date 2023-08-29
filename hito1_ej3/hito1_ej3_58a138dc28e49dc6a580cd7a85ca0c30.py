Ingreso = int(input("ingrese su ingreso en pesos: "))
Año_nacimiento = int(input("ingrese su año de nacimiento: "))
hijos = int(input("ingrese cuantos hijos tiene: "))
año_banco = int(input("ingrese cuantos años pertenece al banco: "))
estado_civil = str(input("mencione cual es su estado civil, si es soltero (s) o casado: " ))
vivienda = str(input("mencione si vive en zona R (rudal) o en zona U (urbana): "))
edad = 2021 - Año_nacimiento
if Ingreso < 0:
    print("el ingreso no puede ser negativo, intentelo de nuevo")
elif Ingreso == 0:
    print("el ingreso no puede ser cero, intentelo otra vez")
elif Año_nacimiento > 2021:
    print("error, intente poner un año de nacimiento valido")
elif hijos < 0:
    print("nadie tiene una cantidad negativa de hijos")
else:
    if año_banco > 10 and hijos >= 2:
        print("APROBADO")
    elif estado_civil == "C" and hijos > 3 and 45 < edad < 55:
        print("APROBADO")
    elif Ingreso > 2500000 and estado_civil == "S" and vivienda == "U":
        print("APROBADO")
    elif Ingreso > 3500000 and año_banco > 5:
        print("APROBADO")
    elif vivienda == "R" and estado_civil == "C" and hijos < 2:
        print("APROBADO")
    else:
        print("RECHAZADO")