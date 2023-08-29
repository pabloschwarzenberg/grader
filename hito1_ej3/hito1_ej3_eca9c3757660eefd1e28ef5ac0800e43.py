#Aprobación de créditos
ingreso=int(input("Ingrese el sueldos:"))
ano=int(input("año de nacimiento:"))
edad=2021-ano
hijos=int(input("nro de hijos:"))
antiguo=int(input("años de permanencia al banco:"))
casado="C"
soltero="S"
estado=input("estado civil:")
campo="R"
ciudad="U"
vive=input("donde vive:")

if antiguo>10 and hijos>=2:
    print("APROBADO")

elif estado==casado and hijos>3 and (edad>=45 and edad<=55):
    print("APROBADO")

elif ingreso>3500000 and antiguo>5:
    print("APROBADO")
    
elif ingreso>2500000 and estado==soltero and vive==ciudad:
    print("APROBADO")

elif vive==campo and estado==casado and hijos<2:
    print("APROBADO")

else:
   print("RECHAZADO")
