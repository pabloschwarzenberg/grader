#Hito 1 creditos
ingresos=(int(input("Ingrese sus ingresos: ")))
nacimiento=(int(input("Ingrese su edad: ")))
hijos=(int(input("ingrese su numero de hijos: ")))
banco=(int(input("Ingrese cuantos años lleva con el banco: ")))
estado=(input("Ingrese su estado civil (S para soltero y C para casado): "))
casa=(input("Ingrese R si vive en campo o U si vive en ciudad: "))

if banco > 10 and hijos >= 2:
          print("APROBADO")
elif estado == 'C' and hijos >= 3 and nacimiento >= 45 and nacimiento <= 55:
          print("APROBADO")
elif ingresos >=2500000 and estado == 'S' and casa == 'U':
          print("APROBADO")
elif ingresos >= 3500000 and banco >= 5:
          print("APROBADO")
elif casa == 'R' and estado == 'C' and hijos <= 2:
          print("APROBADO")
else:
          print("RECHAZADO")
