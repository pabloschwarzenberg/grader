ingresos= int(input("Ingresos (pesos): "))
año= int(input("Año de nacimiento: "))
hj= int(input("Numero de hijos: "))
apb= int(input("Años que pertenecio al banco: "))
Ec= str(input('Estado civil ("S": soltero, "C", casado) '))
dnd= str(input('Si vive en campo o ciudad("U": urbano, "R": rural) '))
if apb>10 and hj>=2:
    print("APROBADO")
elif Ec=="C" or Ec=="c" and hj>3 and año>=45 and año<=55:
    print("APROBADO")
elif ingresos>25000000 and Ec=="C" or Ec=="c" and dnd=="U" or dnd=="u":
    print("APROBADO")
elif ingresos>3500000 and apb>5:
    print("APROBADO")
elif dnd=="R" or dnd=="r" and Ec=="C" or Ec=="c" and hj<2:
    print("APROBADO")
    