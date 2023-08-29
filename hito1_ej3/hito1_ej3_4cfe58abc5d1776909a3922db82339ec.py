#Aprobación de créditos
Ingresos = int(input("¿Monto de sus ingresos? $"))
Nacimiento = int(input("¿Año de nacimiento? "))
Hijos = int(input("¿Cuántos hijos tiene? "))
AñosBanco = int(input("¿Cuántos años lleva con nosotros? "))
Estado = input("¿Su estado civil? soltero=S, casado=C ")
Vivienda = input("¿Dondé vive? Urbano=U, Rural=R ")
Edad = (2020 - Nacimiento)

if (10 < AñosBanco and 2 < Hijos):
    print("APROBADO")
    
elif(Estado == "C" and 3 < Hijos and 45 < Edad < 55):
    print("APROBADO")

elif(250000 < Ingresos and Estado == "S" and Vivienda == "U"):
    print("APROBADO")

elif(350000 < Ingresos and 5 < AñosBanco):
    print("APROBADO")

elif(Vivienda == "R" and Estado == "C" and Hijos < 2):
    print("APROBADO")
    
else:
    print("RECHAZADO")