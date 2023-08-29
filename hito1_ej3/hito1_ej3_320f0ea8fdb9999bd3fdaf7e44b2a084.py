#aprobacion de creditos
ingresos = int(input("ingreso (en pesos): "))
nacimiento = int(input("anio de nacimiento: "))
hijos = int(input("cantidad de hijos: "))
tiempo = int(input("anios de cliente en el banco: "))
estado = input("estado civil ("S": soltero, "C", casado): ")
vivienda = input("lugar donde vive ("U": urbano, "R": rural): ")

edad = (2020 -nacimiento)


if tiempo > 10 and hijos => 2 :
    print("Aprobado")
elif estado == "C" or estado =="C" and hijos > 3 and edad >= 45 and edad <= 55:
    print("Aprobado")
elif ingresos > 2500000 or estado =="S" and vivienda =="U":
    print("Aprobado")
elif ingresos > 3500000 or tiempo > 5 :
    print("Aprobado")
elif vivienda =="R" or estado =="C" and hijos < 2:
    print("Aprobado")
