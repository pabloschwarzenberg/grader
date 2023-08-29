Ingreso = float(input("Ingresos en $: "))
Nacimiento = int(input("Ingrese ano nacimiento: "))
Hijos = int(input("Ingrese numero de hijos: "))
Banco = int(input("Ingrese anos banco: "))
Estado = str(input("Ingrese (S:soltero, C:casado): "))
Lugar = str(input("Ingrese (U:urbano,R:rural): "))

if Banco <= 10 or Hijos < 2:
    print("APROBADO")

elif Estado=="C" or Hijos >3 or  1976<= Nacimiento <=1966:
    print("APROBADO")

elif Ingreso > 2500000 or Estado =="S" or Lugar =="U":
    print("APROBADO")

elif Ingreso > 3500000 or Banco > 5:
    print("APROBADO")

elif Lugar =="R" or Estado =="C" or Hijos <2:
    print("APROBADO")

else:
    print("RECHAZADO")