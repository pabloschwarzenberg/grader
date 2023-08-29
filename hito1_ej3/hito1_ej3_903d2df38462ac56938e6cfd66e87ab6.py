ingreso = int(input("ingrese canditad de mensual de dinero:"))
edad = int(input("ingrese su edad: "))
hijos = int(input("numero de hijos: "))
año_banco = int(input("oe machucao cuanto llevai en el banco"))
estado_civil = input(" 'S': soltero, 'C', casado")
localidad = input("'U': urbano, 'R': rural")

if (año_banco  > 10 and hijos >= 2):
    print("APROBADO")
elif (estado_civil == "C" and hijos > 3 and  edad >= 45 and edad <= 55):
    print("APROBADO")
elif (ingreso >= 2500000 and estado_civil == "S" and localidad == "U"):
    print("APROBADO")
elif (ingreso >= 3500000 and año_banco >5):
    print("APROBADO")
elif (localidad == "R" and estado_civil == "C" and hijos < 2  ):
    print("APROBADO")
else:
    print()