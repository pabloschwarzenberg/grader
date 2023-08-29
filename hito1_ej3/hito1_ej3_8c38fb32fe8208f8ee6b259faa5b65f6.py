#Aprobación de créditos
ingreso=float(input("escriba su ingreso:"))
an=float(input("escriba su año de nacimiento:"))
nh=float(input("ingrese el numero de hijos:"))
apb=float(input("cuantos años es cliente del banco:"))
estado=input("ingrese su estado civil. S para soltero o C para casado:")
vive=input("ingrese la viviendo. R para rural o U ara urbano:")

if apb>10 and nh>=2:
    print("APROBADO")
else:
    print("rechazado")
    
if estado=="C" and nh>3 and an<=1963  and an>=1973 :
    print("APROBADO")
else :
    print("rechazado")
if ingreso>2500000 and estado=="S"  and vive=="U":
    print ("APROBADO")
else:
    print("rechazado")
if ingreso>3500000 and apb>5:
    print("APROBADO")
else:
    print("rechazado")
if vive=="R" and  estado=="C" and nh<2:
    print("APROBADO")
else:
    print("rechazado")     