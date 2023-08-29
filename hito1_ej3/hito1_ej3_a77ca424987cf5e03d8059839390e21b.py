#Aprobación de créditos
ingresos = float(input("Ingresos: "))
año = int(input("Año en que naciste: "))
hijos = int(input("Numero de hijos: "))
añob = int(input("Años con el banco: "))
estado = str(input("Estado civil(S para soltero, C para casado): "))
vive = str(input("Donde vives(U para urbano, R para rural): "))
if añob >=10 and hijos>=2:
    print("APROBADO")
elif estado == "C" or estado =="c" and hijos >=3 and año >=45 or año <=55:
    print("APROBADO")
elif ingresos >2500000 and estado =="S" or estado =="s" and vive =="U" or vive =="u":
    print("APROBADO")
elif ingresos >3500000 and añob >= 5:
    print("APROBADO")
elif vive =="R" or vive =="r" and estado =="C" or estado == "c" and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")
       