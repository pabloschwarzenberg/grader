from datetime import date
ingreso=int(input("ingrese cantidad de ingreso en pesos: "))
año_nacimiento=input("ingrese año nacimiento separado de: ")
hijos=int(input("ingrese cantidad de hijos/as: "))
años=int(input("ingrese años de pertenencia en el banco: "))
estado_civil=input("ingrese estado civil S(soltero)/C(casado): ")
vive=input("ingrese si vive en lo Urbano o Rural U/R: ")

edad=0
def edad(año_nacimiento):
    fecha_Actual=date.today.year()
    edad=fecha_Actual-año_nacimiento
    return edad

while True:
    if años<=10 and hijos<=2:
        print("Aprovado")
    elif estado_civil=="c" or "C" and hijos<=3 and edad<=45>55:
        print("Aprovado")
    elif ingreso<=2500000 and estado_civil=="s" or "S" and vive=="u" or "U":
        print("Aprovado")
    elif ingreso<=3500000 and años<=5:
        print("Aprovado")
    elif vive=="r" or "R" and estado_civil=="C" or "c" and hijos>=2:
        print("Aprovado")   
    else: 
        print("rechazado")
    break