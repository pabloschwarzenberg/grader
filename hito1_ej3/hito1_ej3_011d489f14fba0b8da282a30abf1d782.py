x=int(input(" ingreso(en pesos): "))
y=int(input("año de nacimiento :"))
z=int(input("numero de hijos:"))
a=int(input("años de pertenencia al banco :"))
e=input("S:soltero, C: casado: : ")
v=input("U:urbano, R:rural: ")

años= 2021-y
   

if a>10 and  z>=2:
   print("APROBADO")


if e =="C" and z>3 and años>=45 and años<=55 :
    print("APROBADO")

    
if x > 2500000 and  e=="S" and v=="U":
    print("APROBADO")
    


if x>3500000 and a>5:
    print("APROBADO")
    


if v=="R" and e=="C" and z<2:
   print("APROBADO")

else:
    print ("RECHAZADO")