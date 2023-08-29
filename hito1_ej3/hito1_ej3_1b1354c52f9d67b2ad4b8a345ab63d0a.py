#Aprobación de créditos
pesos = int(input("Escriba su ingreso en pesos: "))
nacimiento = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese su cantidad de hijos: "))
anos = int(input("Ingrese los años de pertenencia al banco: "))
casado = input("Ingrese su estado civil S para soltero C para casado: ")
vive = input("Ingrese si vive en campo o ciudad U para urbano or R para rural: ")
anoscliente = 2023 - nacimiento



if anos > 10 and hijos >= 2:
    print("APROBADO")
elif casado == "C" and hijos > 3  and  45 < añoscliente < 55:
    print("APROBADO")
elif pesos > 2500000 and casado == "S" and vive == "U": 
    print("APROBADO")
elif pesos > 3500000 and años > 5:
    print("APROBADO")
elif vive == "R" and casado == "C" and  hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")      