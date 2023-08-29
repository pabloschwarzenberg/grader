#Aprobación de créditos
print("Bienvenidos")
ingresos=int(input("Cuales son sus ingresos?"))
edad=input("año de nacimiento?")
hijos=input("numero de hijos?")
anos_en_el_banco=input("cuantos años lleva en el banco?")
estado_civil=input("Soltero o Casado?")
donde_vive=input("vive en el campo o la ciudad?")

if (int(anos_en_el_banco)>10 and int(hijos)>=2):
    print("APROBADO")
elif (estado_civil=="C" and int(hijos)>3 and 1965>int(edad)>1955):
    print("APROBADO")
elif (ingresos>2500000 and estado_civil=="S" and donde_vive=="U"):
    print("APROBADO")
elif (ingresos>3500000 and int(anos_en_el_banco)>5):
    print("APROBADO")
elif (donde_vive=="R" and estado_civil=="C" and int(hijos)<2):
    print("APROBADO")

else:
    print("REPROBADO")
    




