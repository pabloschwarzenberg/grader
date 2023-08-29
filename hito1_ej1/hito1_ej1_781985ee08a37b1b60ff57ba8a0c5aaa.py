#Nota final
#Desarrollar un programa que calcule nota final.

pt=float(input("Ingrese nota de tareas: "))
pi=float(input("Ingrese nota de interrogaciones: "))
ne=float(input("Ingrese nota de pruebas: "))
pp=float(input("Ingrese notas de presentación: "))

#Cálculo:

calculo=(0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp)

#Final:
if calculo>=4:
  print(round("Su nota final del curso es: ")), (calculo,1)

else:
  calculo<=3.9
  print(round("Su nota final es: ")), (calculo,1), (", por ende, debe repetir año.")