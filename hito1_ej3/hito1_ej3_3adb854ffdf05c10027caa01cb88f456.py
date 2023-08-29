#Aprobación de créditos
ingreso= int(input("ingrese sus ingresos: "))
años = int(input("Ingrese el año de nacimiento: "))
hijos= int(input("Ingrese la cantidad de hijos: "))
añopert = int(input("Ingrese los alños que lleva en el banco: "))
estcivil = input("Ingrese su estado civil(S: soltero, C: casado): ")
camp = input("Ingrese donde vive campo o cuidad (U: urbano, R: rural): ")

edad = 2021 - años

if añopert >= 10 and hijos >= 2:
    print("APROBADO")


elif estcivil == "C" and hijos >= 3 and edad in range(45, 55):
    print("APROBADO")

elif ingreso >= 2500000 and estcivil == "S" and camp == "U" :
    print("APROBADO")

elif ingreso >= 3500000 and añopert >= 5:
    print("APROBADO")

elif camp == "R" and hijos <=2:
    print("APROBADO")       