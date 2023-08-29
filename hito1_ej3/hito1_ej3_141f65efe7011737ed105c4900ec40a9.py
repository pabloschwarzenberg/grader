#Aprobación de créditos
ingreso=float(input("ingrese monto en pesos: "))
año_nacimiento=int(input("ingrese año de nacimiento: "))
edad=2021-año_nacimiento
numero_hijos=int(input("ingrese numero de hijos: "))
año_per_banco= int(input("ingrese año de pertenencia al banco: "))
estado=input("ingrese estado civil (S:soltero, C:casado)")
vivienda=str(input("ingrese donde vive (U:urbano, R:rural)"))

if año_per_banco >= 10 and numero_hijos >= 2:
    print("APROBADO")
elif ((estado == "C" or estado == "C") and numero_hijos >= 3 and (edad >= 45 and edad <= 55)):
    print("APROBADO")
elif (ingreso >= 2500000 and (estado =="S" or estado =="S") and (vivienda == "U" or estado == "U")):
    print("APROBADO")
elif(ingreso > 3500000 and año_per_banco >5):
    print("APROBADO")
elif (vivienda == "U" or vivienda == "R") and (estado == "C") and numero_hijos <= 2:
    print ("APROBADO")
else:
    print("DESAPROBADO")