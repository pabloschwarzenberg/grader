#Aprobación de créditos
ingreso = int(input("Ingrese su sueldo en pesos: "))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = int(2021 - anio_nacimiento)
cantidad_hijos = int(input("Ingrese cantidad de hijos: "))
anios_banco = int(input("Ingrese la cantidad de años que lleva en este banco: "))
estado_civil = input("Indique su estado civil (S) soltero / (C) casado: ")
estado_civil= estado_civil.upper()
localidad = input("Indique donde vive (U) urbano / (R) rural: ")
localidad = localidad.upper()


if anios_banco> 10 and cantidad_hijos >= 2:
    print ("APROBADO")
elif estado_civil == "C" and cantidad_hijos> 3 and edad >= 45 and edad <= 55 :
    print ("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and estado_civil== "U":
    print ("APROBADO")
elif ingreso > 3500000 and anios_banco > 5:
    print ("APROBADO")
elif localidad == "R" and estado_civil == "C" and cantidad_hijos < 2:
    print ("APROBADO")
else:
    print ("RECHAZADO")