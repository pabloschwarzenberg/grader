#Aprobación de créditos
I=    int(input("ingrese sus ingresos:"))
FC=   int(input("ingresar su fecha de nacimiento:"))
NH=   int(input("ingresar numero de hijos:"))
AA=   int(input("ingresar años de antiguedad:"))
EC=   str(input("ingresar estado civil (S: soltero, C, casado):"))
COC=  str(input("ingresar localidad(U: urbano, R: rural):"))

FC2= (2021-FC)
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if (AA>10) and (NH>=2):
    print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif (EC=="S") and (NH>3) and (FC2>45) and (FC2<55):
    print ("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif (I>2500000) and (EC=="S") and (COC=="U"):
    print ("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif (I>3500000) and (AA>5):
    print ("APROBADO")
elif (COC=="R") and (EC=="C") and (NH<2):
    print ("APROBADO")
else:
    print("DENEGADO")