#Aprobación de créditos
ingreso = int(input("Ingreso en pesos: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Número de hijos: "))
añosPertenenciaBanco = int(input("Años de pertenencia al banco: "))
estadoCivil = input("Estado civil(S: soltero, C: casado): ")
zonaVivienda = input("Urbano(U) o Rural(R): ")

if añosPertenenciaBanco > 10 and hijos >= 2:
    print("APROBADO")
    
elif estadoCivil == "C" and hijos > 3 and 45 >= 2023-nacimiento <= 55:
    print("APROBADO")
    
elif ingreso > 2500000 and estadoCivil == "S" and zonaVivienda == "U":
    print("APROBADO")
    
elif ingreso > 3500000 and añosPertenenciaBanco > 5:
    print("APROBADO")
    
elif zonaVivienda == "R" and estadoCivil == "C" and hijos < 2:
    print("APROBADO")
    
else:
    print("RECHAZADO")    