#Aprobación de créditos
print("aprobacion de crédito")

Ingreso = eval(input("Ingrese el monto de su sueldo: "))

Nacimiento = eval(input("Ingrese año de nacimiento: "))

Hijos = eval(input("Ingrese cantidad de hijos: "))

Banco = eval(input("Ingrese años de pertenencia al banco: "))

Estado = str(input("Ingrese estado civil: (S: soltero, C: casado)"))

Lugar = str(input("Ingrese zona en la que vive: (U: urbano, R: rural)"))

Años = 2021 - Nacimiento
                  
Contador = 0
if((Banco > 10) and (Hijos >= 2)):
                  Contador = Contador + 1

elif((Estado == "C") and (Hijos > 3) and (Años > 45) and (Años < 55)):
                  Contador = Contador + 1

elif((Ingreso > 2500000) and (Estado == "S") and (Lugar == "U")):
                  Contador = Contador + 1

elif((Ingreso > 3500000) and (Banco > 5)):
                  Contador = Contador + 1

elif((Lugar == "R") and (Estado == "C") and (Hijos < 2)):
                  Contador = Contador + 1


if(Contador >= 1):
 print("Cumple con ",Contador," requerimientos")
 print("APROBADO")

else:
    print("Cumple con ",Contador," requerimientos")
    print("RECHAZADO")      