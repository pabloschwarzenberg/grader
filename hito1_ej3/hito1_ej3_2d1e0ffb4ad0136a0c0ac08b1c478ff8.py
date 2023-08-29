print("ingresos")
ingresos = eval(input())
print("ingrese su año de nacimiento")
año = eval(input())
print("ingre su cantidad de hijos")
hijos = eval(input())
print("años en el banco")
banco = eval(input())
print("usted esta casado o soltero")
estado = str(input())
print("donde vive urbano o rural")
donde = str(input())

casado = "C"
soltero = "S"

urbano = "U"
rural = "R"
edad = año - 2020
#aprueba

if(banco >= 10) and (hijos >= 2):
    print("APROBADO")
else:
    if(estado == "C") and (hijos > 3) and (edad >= 45) and (edad <= 55):
        print("APROBADO")
    else:
        if(ingresos > 2500000) and (estado == "S") and (donde == "U"):
            print("APROBADO")
        else:
            if(ingresos > 3500000) and (banco > 5):
                print("APROBADO")
            else:
                if(donde == "R") and (estado == "C") and (hijos < 2):
                    print("APROBADO")
                else:
                    print("RECHAZADO")