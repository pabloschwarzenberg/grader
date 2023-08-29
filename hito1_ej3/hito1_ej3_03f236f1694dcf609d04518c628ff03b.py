Ingreso=int(input("Ingresos en pesos: \n"))
nacimiento=int(input("Fecha de nacimieto: \n"))
hijos=int(input("Cuantos hijos tiene: \n"))
banco=int(input("Años afiliado al banco: \n"))
Estado_civil=input("Estado civil, S o C: \n")
vivienda=input("vive en campo(Rural) o cuidad(Urbano), R  o U: \n")

edad=2022-nacimiento

if banco > 10 and hijos>=2:
  print("APROBADO")
elif Estado_civil == "C" and hijos>3 and  edad>=45 and edad<=55:
  print("APROBADO")
elif Ingreso>2500000 and  Estado_civil =="S" and vivienda == "U":
  print("APROBADO")
elif Ingreso>3500000 and banco >5:
    print("APROBADO")
elif vivienda=="R" and Estado_civil=="C" and hijos<2:
    print("APROBADO")
else:
  print("Rechazado")