#Aprobación de créditos
from datetime import date

print("Ingresar los siguientes datos")

ingreso=eval(input("Indicar su ingreso en pesos: "))
nacimiento=int(input("Ingresar su año de nacimiento: "))
hijos=int(input("Ingrese su numero de hijos: "))
pertenencia=eval(input("Ingrese sus años de pertenencia al banco: "))
estado=input("Ingrese su estado civil soltero o casado: ")
vivir=input("Ingrese lugar de vivienda urbano o rural: ")

caso1 = pertenencia + hijos

if caso1 >= 13:
    print("Credito Aprobado")
else:
    print("Credito Rechazado")

caso2 = estado
caso2 = hijos
caso2 = nacimiento
def calcular_edad_agnios(nacimiento):
    fecha_actual = date.today()
    edad = fecha_actual.year - nacimiento.year
    return edad
    print(edad)


if caso2 == casado:
    if caso2 > 3:
        if 45 <= caso2 <= 55:
            print("Credito Aprobado")
        else:
            print("Credito Rechazado")      