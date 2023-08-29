#Aprobación de créditos
ingreso=int(input("ingrese sus ingresos"))
año_n=int(input("ingrece su año de nacimiento"))
hijos=int(input("ingrese su numero de hijos"))
años_p=int(input("ingrese sus años de pertenencia al banco"))
estado_c=input("ingrese su estado civil, S si es soltero o C si es casado")
vive=input("ingrese U si vive en la ciudad o R si vive en el campo")
edad=2017-año_n
if años_p>10 and hijos>=2:
    print("APROBADO")
elif estado_c=="C" and hijos>3 and edad>=45 and edad<=55:
    print("APROBADO")  
elif ingreso>2500000 and estado_c=="S" and vive=="U":
    print("APROBADO")
elif ingreso>3500000 and años_p>5:
    print("APROBADO")
elif vive=="R" and estado_c=="C" and hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")
