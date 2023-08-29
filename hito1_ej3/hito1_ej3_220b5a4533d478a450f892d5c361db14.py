pesos = int(input("Ingrese el ingreso en pesos: "))
años = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese cuantos hijos tiene: "))
banco = int(input("Ingrese la cantidad de años dentro del banco: "))
estado = str(input("Ingrese si esta soltero (S) o casado(C): "))
ciudad = str(input("Ingrese si vive en campo(R) o ciudad(U): "))
edad = (2020-años)
if (banco>= 10) and (hijos >= 2):
    print("APROBADO")
elif (estado =="ciudad") and (hijos>=3) and (45<=edad<=55):
    print("APROBADO")
elif (pesos>=2500000) and (estado == "S") and (ciudad == "U"):
    print("APROBADO")
elif (pesos>=350000) and (banco>=5):
    print("APROBADO")
elif (ciudad == "R") and (estado == "C" ) and (hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")     