#nombre: Zhunyi Ma
##Entrada de datos 

##Datos a rellenar
print("Gracias por usar nuestros servicios, a continuacion complete los siguientes datos: ")
print("-------------------------------------------")
ingr = int(input("Ingrese la cantidad de sus ingresos mensuales en pesos: $"))
an = int(input("Ingrese AÑO de nacimiento: "))
hijos = int(input("Ingrese el numero de HIJOS: "))
anbanco = int(input("Cuando años lleva siendo socio del banco?: "))
soltero = "S"
casado = "C"
estadoc = input("Estado civil   -'S' para soltero y 'C' para casado-: ")
edada = 2022-an
##Procesos
if estadoc == "S":
  print("Usted es SOLTERO")
elif estadoc == "C":
  print("Usted es CASADO")

campo = "R"
ciudad = "U"
viv = input("Usted vive en campo o ciudad? 'U' para ciudad y 'R' para campo: ")
print("-------------------------------------------")
if anbanco > 10 and hijos > 2:
   print("APROBADO")
elif estadoc == "C" and hijos > 3 and  edada >45 and edad <55:
 print("APROBADO")
elif ingr > 2500000 and estadoc == "S" and viv == "U": 
 print("APROBADO")
elif ingr > 3500000 and anbanco > 5:
 print("APROBADO")
elif viv == "R" and estadoc == "C" and hijos < 2 and hijos > 0:
 print("APROBADO")
else:
 print("REPROBADO")