#Aprobación de créditos
ingreso=int(input("ingreso en pesos: "))
año=int(input("año de nacimiento: "))
hijos=int(input("numero de hijos: "))
banco=int(input("años de pertenencia al banco: "))
civil=input("ingrese su estado civil (S:soltero,C:casado): ")
lugar=input("ingrese si vive en campo o ciudad (U:urbano,R:rural): ")

#aprobación del credito
if (banco>10) and (hijos>=2):
    print("APROBADO")
elif (civil == "C") and (hijos>3) and ((2020-año)>45 and (2020-año)<55):
    print("APROBADO")
elif (ingreso>2500000) and (civil == "S") and (lugar == "U"):
    print("APROBADO")
elif (ingreso>3500000) and (banco>5):
    print("APROBADO")
elif (lugar == "R") and (civil == "C") and (hijos<2):
    print("APROBADO")
else:
    print("RECHAZADO")    