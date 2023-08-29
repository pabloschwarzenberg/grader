#Aprobación de créditos
ingreso = int(input("Ingresos que posee: $"))
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
numero_hijos = int(input("¿Cuantos hijos tiene?: "))
anio_banco = int(input("Ingrese la cantidad de años que pertenece al banco: "))
estado_civil = str(input("Ingrese su estado Civil, S (soltero), C(casado): "))
donde_vive = str(input("Vive en el campo o en ciudad (U: urbano, R: rural): "))

edad = 2020 - anio_nacimiento 
if anio_banco > 10 and numero_hijos >= 2:
    print("Credito de consumo APROBADO")
elif estado_civil.upper() == "C" and numero_hijos >= 3 and  (edad >= 45 and edad <= 55):
    print("Credito de consumo APROBADO")
elif ingreso > 2500000 and estado_civil.upper() == "S" and donde_vive.upper() == "U":
    print("Credito de consumo APROBADO")
elif ingreso > 3500000 and anio_banco > 5:
    print("Credito de consumo APROBADO")
elif donde_vive.upper() == "R" and estado_civil.upper() == "C" and numero_hijos <= 1:
    print("Credito de consumo APROBADO")
else:
    print("Credito de consumo RECHAZADO")