ing = float(input("Indique su ingreso mensual (en pesos): "))
año = int(input("Ingrese su año de nacimiento: "))
nhijos = int(input("Ingrese la cantidad de hijos que tiene: "))
añobanco = input("¿A cúantos años esta en nuestro banco?: ")
et = input("¿Cúal es su estado civil? (ingrese S para soltero o C para casado): ")
ur = input("Indique si vive en campo o ciudad (U para urbano y R para rural:")
edad = 2020-año

if (et == "C" and nhijos > 3):
    print("APROBADO")
elif(edad >= 45 and edad <= 55):
    print("APROBADO")
else:
    print("RECHAZADO")

if(ing>2500000):
    print("APROBADO")
elif(et == "S" and ur == "U"):
    print("APROBADO")
else:
    print("RECHAZADO")

if(ing>3500000 and añobanco<5):
    print("APROBADO")
else:
    print("RECHAZADO")

if(ur == "R" and et == "C"):
    print("APROBADO")
elif(nhijos== 0 or nhijos== 1):
    print("APROBADO")
else:
    print("RECHAZADO")