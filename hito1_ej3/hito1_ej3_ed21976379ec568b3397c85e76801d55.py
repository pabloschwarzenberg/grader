pesos = int(input("Ingrese pesos :"))
nacimiento = int(input("Ingrese año de nacimiento :"))
hijos = int(input("Ingrese numero de hijos :"))
pertenencia = int(input("Ingrese cuantos años lleva en el banco :"))
print("   S : Soltero    C : Casado")
estadocivil = str(input("Ingese su estado civil:"))
print("   U : Urbano    R : Rural")
localidad = str(input("Ingrese su localidad :"))

edad = 2019 -nacimiento



if((pertenencia > 10)and(hijos >= 2)):
        print("APROBADO")
elif((estadocivil == "C")and(hijos > 3)and(edad >= 45 and edad <= 55)):
            print("APROBADO")
elif((pesos > 2500000)and(estadocivil == "S")and(localidad == "C")):
            print("APROBADO")
elif((pesos > 3500000)and(pertenencia > 5)):
       print("APROBADO")
elif((localidad == "R")and(estadocivil == "C")and(hijos < 2)):
            print("APROBADO")
else:
    print("RECHAZADO")