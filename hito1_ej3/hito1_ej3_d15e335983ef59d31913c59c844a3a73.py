#Aprobación de créditos
ingreso = int(input("ingreso: "))
año = int(input("año de nacimiento: "))
hijos = int(input("numero de hijos: "))
antiguedad = int(input("años de pertenencia al banco: "))
estado = input("estado civil (S: soltero, C: casado) : ")
lugar = input("residencia (U: urbano, R: rural) : ")
edad = 2023 - año

if antiguedad >= 10 and hijos >= 2:
    print("APROBADO")
elif estado == ("C" or "c") and hijos > 3 and edad <= 55 and edad >= 45:
    print("APROBADO")
elif ingreso >= 2500000 and estado == ("S" or "s") and lugar == ("U" or "u"):
    print("APROBADO")
elif ingreso >= 3500000 and antiguedad > 5:
    print("APROBADO")
elif lugar == ("R" or "r") and estado == ("C" or "c") and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")