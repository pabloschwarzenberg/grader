#Aprobación de créditos
ingreso = int (input("ingrese su ingreso: "))
ano = int(input("ingrese su ano de nacimiento: "))
hijos = int(input("ingrese numero de hijos: "))
ano_banco = int(input("cuantos anos ha pertenecido al banco?: "))
estado_civil = input("esta soltero o casado?: ")
campo_ciudad = input("vive en campo o ciudad "U" urbano, "R" rural:")
edad = 2020 - ano

if ano_banco >= 10 and hijos >= 2:  
    print("APROBADO")

elif estado_civil == "C" and hijos > 3 and 45 < edad < 55:      
    print("APROBADO")

elif ingreso > 2500000 and estado_civil == "S" and campo_ciudad == "U": 
    print("APROBADO")

elif ingreso > 3500000 and ano_banco > 5:
    print("APROBADO")

elif campo_ciudad == "R" and estado_civil == "C" and hijos < 2:
    print ("APROBADO")

else:
    print("RECHAZADO")      