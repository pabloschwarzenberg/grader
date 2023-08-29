Sueldo = int(input("Ingrese su sueldo: "))
Nacimiento = int(input("Ingrese su año de nacimiento: "))
Hijos = int(input("Ingrese la cantidad de hijos que tiene: "))
Pertenencia = int(input("Ingresa tus años de pertenencia en el banco: "))
Estado = str(input("Ingrese si es casado (C) o soltero (S): "))
Residencia = str(input("Ingrese si vive en la ciudad (U) o campo (R): "))

fecha = 2021
Edad = (Nacimiento - fecha)
Resultado = (Edad * -1)

if Pertenencia > 10 and Hijos >= 2:
    print("APROBADO")
elif Estado == "C" and Hijos > 3 and Edad > 45 and Edad <55:
  print("APROBADO")
elif Resultado <= 45 and Resultado <= 55:
  print("APROBADO")
        
  
elif Estado == "s" or Estado == "S":
    if Residencia == "U" or Residencia == "u":
        if Sueldo >= 250000:
            print("APROBADO")
        else:
            print("RECHAZADO")
    else:
        print("RECHAZADO")
elif Pertenencia > 5:
    if Sueldo >= 350000:
        print("APROBADO")
    else:
        print("RECHAZADO")
elif Residencia == "r" or Residencia == "R":
    if Estado == "C" or Estado == "c":
        if Hijos < 2:
            print("APROBADO")
        else:
            print("RECHAZADO")
    else:
        print("RECHAZADO")
else:
    print("RECHAZADO")