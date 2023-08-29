#Aprobación de créditoS
ing=int(input("ingrese su ingreso en pesos: "))
año=int(input("ingrese su año de nacimiento: "))
numhijos=int(input("ingrese su cantidad de hijos: "))
apb=int(input("ingrese la cantidad de años que ha pertenecido a este banco: "))
civil=input("ingrese una'S' si su estado civil es soltero e ingrese una 'C' si su estado civil es casado: ")
vive=input("ingrese una 'U' si vive en la ciudad e ingrese una 'R' si vive en el campo: ")
if apb>10 and numhijos>=2 or civil=="C" and numhijos>3 and año==[1967,1977] or ing>2500000 and civil=="S" and vive=="U" or ing>3500000 and apb>5 or vive=="R" and civil=="C" and numhijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")