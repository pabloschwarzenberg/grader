#Aprobación de créditos
ingreso=int(input("Ingrese el monto de sus ingresos (pesos): "))
nacimiento=int(input("Ingrese su año de nacimiento: "))
hijos=int(input("Ingrese la cantidad de hijos: "))
año_banco=int(input("Ingrese los años de pertenencia al banco: "))
estado_civil=(input("Ingrese si estado civil:  Soltero(S) - Casado(c)"))
residencia=(input("Ingrese si vive en campo (R) o ciudad (U)"))

edad=2022-nacimiento

if año_banco>=10 and hijos>=2:
    print("APROBADO")
elif estado_civil=="C" and hijos>=3 and edad>=45 and edad<=55:
    print("APROBADO")
elif ingreso>=2500000 and estado_civil=="S" and residencia =="U":
    print("APROBADO")
elif ingreso>=3500000 and año_banco>=5:
    print("APROBADO")
elif residencia=="R" and estado_civil=="C" and hijos<=2:
    print("APROBADO")
else:
    print("RECHAZADO")