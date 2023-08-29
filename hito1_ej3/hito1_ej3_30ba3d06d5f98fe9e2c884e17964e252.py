#Aprobación de créditos

Ingreso = int(input("Ingrese su sueldo en pesos "))
Ano_de_nacimiento = int(input("ingrese su Año de Nacimiento "))
Numero_de_hijos = int(input("Ingrese su numero de hijos "))
Anos_de_pertenencia = int(input("Ingrese sus años de pertenencia al Banco "))
Estado_Civil = str(input("ingrese su estado civil (S) soltero o (C) Casado: "))
Donde_vive = str(input("Vive en campo (R) o ciudad (U): "))


Ano_actual = 2022
Edad = Ano_actual - Ano_de_nacimiento
if Anos_de_pertenencia > 10 and Numero_de_hijos >= 2:
    print("Aprobado")
elif str(Estado_Civil) == "C" and Numero_de_hijos > 3 and Edad < 55 and Edad > 45:
    print("Aprobado")
elif Ingreso > 2500000 and str(Estado_Civil) == "S" and str(Donde_vive) == "U":
    print("Aprobado")
elif Ingreso > 3500000 and Anos_de_pertenencia > 5:
    print("aprobado")
elif str(Donde_vive) == "R" and str(Estado_Civil) == "C" and Numero_de_hijos < 2:
    print("Aprobado")
      