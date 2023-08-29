ingresos=int(input("ingreso en pesos: "))
año=int(input("año de nacimiento: "))
hijos=int(input("numero de hijos: "))
banco=int(input("años de pertenencia al banco: "))
civil=str(input("estado civil S o C: "))
urbano=str(input("urbano o rural U o R: "))
años=2021-año
if banco>10 and hijos>=2:
    print("APROBADO")
elif(civil=="C" or civil=="c") and (hijos>3) and (años>=45 and años<55):
    print("APROBADO")
elif(ingresos>2500000) and (civil=="S" or civil=="s") and (urbano=="U" or urbano=="u"):
     print("APROBADO")
elif((ingresos>3500000) and (banco>5)):
     print("APROBADO")
elif(urbano=="R" or urbano=="r") and (civil=="C" or civil=="c") and (hijos<2):
     print("APROBADO")
else:
     print("RECHAZADO")     