i = input( " Escribir ingreso (en pesos) : ")
i = int(i)
an = input( " Ingresar año de nacimiento: ")
an = int(an)
nh = input( " Ingresar número de hijos: ")
nh = int(nh)
pb = input( " Ingresar años de pertenencia al banco: ")
pb = int(pb)
e = input( " Ingresar estado civil ( S: soltero, C: casado): ")
v = input( " Ingresar domicilio ( U: urbano, R: rural): ")


if pb > 10 and nh >= 2:
 print( " APROBADO ") 
elif e == "C" and nh > 3 and  1962 < an > 1972:
 print( " APROBADO  ")
elif i > 2500000 and e == "S" and v == "U":
 print( " APROBADO ")
elif i > 3500000 and pb > 5:
 print( " APROBADO  ")
elif v == "R" and e == "C" and nh < 2:
 print( " APROBADO ")

else:
 print( " RECHAZADO ")


