#Aprobación de créditos
ingreso = int(input("Ingrese su salario: "))
edad = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese su número de hijos: "))
pertenencia = int(input("Ingrese sus años de pertenencia al banco: "))
edo = input("Ingrese su estado civil (S/C): ")
vivienda = input("Ingrese su lugar de vivienda (U/R): ")

if pertenencia > 10 and hijos >= 2:
    print("APROBADO")
elif edo == "C" or "c" and hijos > 3 and 45 <= (edad - 2021) <= 55:
    print("APROBADO")
elif ingreso > 2500000 and edo == "S" or "s" and vivienda == "U" or "u":
    print ("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" or "r" and edo == "C" or "c" and hijos < 2:
    print("APROBADO")
else:
    print("SACATE!")