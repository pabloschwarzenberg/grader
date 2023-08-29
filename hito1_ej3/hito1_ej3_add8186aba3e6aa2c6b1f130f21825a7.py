Ingresos = int(input("Ingrese sus ingresos mensuales en pesos"))
Nacimiento = int(input("Ingrese su año de nacimiento"))
Hijes = int(input("Ingrese su número de hijos"))
Años = int(input("¿Cuántos años lleva siendo parte del banco?"))
Estado = str(input("Ingrese 'S' si es soltero o 'C' si es casado"))
campoCiudad = str(input("Ingrese 'U' si vive en zona urbana o 'R' si vive en zona rural"))
Edad = 2020 - Nacimiento

if Años >= 10 and Hijes >= 2:
    print("APROBADO")
elif Estado == "C" and Hijes > 3 and 45 <= Edad <= 55:
    print("APROBADO")
elif (Ingresos > 2500000 and Estado == "S" and
      campoCiudad == "U"):
    print("APROBADO")
elif Ingresos > 3500000 and Años >= 5:
    print("APROBADO")
elif campoCiudad == "R" and Estado == "C" and Hijes < 2:
    print("APROBADO")
else:
    print ("RECHAZADO")


##O tambien puede ser, siguiendo con las mismas definiciones de arriba

##if ((Años >= 10 and Hijes >= 2) or (Estado == "C" and Hijes > 3 and 45 <= Edad <= 55) or
##    (Ingresos > 2500000 and Estado == "C" and campoCiudad == "U") or
##    (Ingresos > 3500000 and Años >= 5) or
##    (campoCiudad == "R" and Estado == "C" and Hijes < 2)):
##    print("APROBADO")
##else:
##    print("RECHAZADO")

    
    