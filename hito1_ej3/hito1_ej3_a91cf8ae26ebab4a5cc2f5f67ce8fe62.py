#Aprobación de créditos
ingreso = float(input("Digite ingreso en pesos: "))
año_nac = int(input("Ingrese año: "))
num_hijos = int(input("Ingrese el número de hijos: "))
años_banco = int(input("Ingrese los años de pertenencia al banco: "))
estado_civil =input("Ingrese S si es soltero y C si es casado: ")
zona = input("Ingrese zona: Si vive en el campo (R), si vive en la ciudad (U): ")

if años_banco > 10:
    print("APROBADO")
elif estado_civil == "C" and num_hijos >3 and año_nac >= 45 and año_nac <=55:
    print("APROBADO")
elif ingreso> 2500000 and estado_civil == "S" and años_banco >5 == "U":
    print("APROBADO")
elif ingreso> 3500000 and años_banco >5: 
    print("APROBADO")  
elif estado_civil == "C" and zona == "R" and num_hijos <2:
    print("APROBADO")

else:
    print("RECHAZADO")
