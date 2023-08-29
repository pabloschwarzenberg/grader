#Aprobación de créditos
ingreso = int(input("Ingrese el monto en pesos: "))
ano = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese el numero de hijos que tiene: "))
anosenelbanco = int(input("Ingrese cuantos años lleva perteneciendo al banco: "))
estado = str(input("Ingrese su estado civil (S= soltero/C= casado): "))
vive = str(input("Ingrese donde vive (U= urbano/R= rural): "))

#Condicionales

if anosenelbanco > 10 and hijos >= 2:
    print("APROBADO")
    
elif (estado == "C" or estado == "c") and (hijos >= 3) and (anos >= 1975 and anos <=1965):
    print("APROBADO")
    
elif (ingreso > 2500000) and (estado == "S" or estado == "s") and (vive == "U" or vive == "u"):
    print("APROBADO")
    
elif (ingreso > 3500000) and anosenelbanco > 5:
    print("APROBADO")
    
elif (vive == "R" or vive == "r") and (estado == "C" or estado == "c") and (hijos < 2):
    print("APROBADO")

else:
    print("Rechazado")