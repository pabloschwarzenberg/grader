#Aprobación de créditos
Ingresos = int(input("Digite sus ingresos: "))
Nacimiento = int(input("Digite su año de nacimiento: "))
Hijos = int(input("Cantidad de hijos: "))
Antiguedad = int(input("Años de pertenencia al banco: "))
Estado = str(input("Soltero o casado: "))
Residencia = str(input("reside en campo o ciudad? : "))
Edad = 2021-Nacimiento

if Antiguedad > 10 and Hijos >= 2:
    print("APROBADO")
elif Antiguedad <= 10 and Hijos < 2:
    print("RECHAZADO")

if Estado == "C" and Hijos > 3 and Edad >= 45 or Edad >= 55:
    print("APROBADO")
elif Estado != "C" and Hijos < 3 and Edad < 45:
    print("RECHAZADO")

if Ingresos > 250000 and Estado == "S" and Residencia == "U":
    print("APROBADO")
elif Ingresos < 250000 and Estado != "S" and Residencia != "U":
    print("RECHAZADO")

if Ingresos > 350000 and Antiguedad > 5:
    print("APROBADO")
elif Ingresos < 350000 and Antiguedad < 5:
    input("RECHAZADO")

if Residencia == "R" and Estado == "C" and Hijos < 2:
    print("APROBADO")
elif Residencia != "R" and Estado != "C" and Hijos > 2:
    print("RECHAZADO")      