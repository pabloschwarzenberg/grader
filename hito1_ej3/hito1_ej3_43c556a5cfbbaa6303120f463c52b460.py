#Aprobación de créditos
print("Aprobador de creditos del Banco")
ingresos = input("Ingreso en pesos: ")
nacimiento = input("Año de nacimiento: ")
hijos = input("Número de hijos: ")
pertenencia = input("Años de pertenencia al banco: ")
estado = input("Estado civil (""S"": soltero, ""C"", casado): ")
localidad = input("¿Vive en campo o cuidad? (""U"": urbano, ""R"": rural): ")

print("¿Son correctos los datos?: \nIngresos: ",ingresos,"\nNacimiento: ",nacimiento,"\nHijos: ",hijos,"\nAños de pertenencia al banco: ",pertenencia,"\nEstado civil: ",estado,"\nLocalidad: ",localidad)

if (int(pertenencia)>10 and int(hijos)>=2) or (estado == "C" and int(hijos) >= 3 and (45<=2016 - int(nacimiento))<=55) or (int(ingresos) > 2500000 and estado == "S" and localidad == "U") or (int(ingresos) > 3500000 and int(pertenencia) > 5) or (localidad == "R" and estado == "C" and int(hijos) < 2):
    print("APROBADO")

else:
    print("RECHAZADO")

