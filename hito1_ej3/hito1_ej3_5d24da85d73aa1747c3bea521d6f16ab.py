#Aprobación de créditos
ingreso=int(input("INGRESOS: "))
year= int(input("AÑO NACIMIENTO: "))
hijos=int(input( "Nº DE HIJOS: "))
añosbanco=int(input("AÑOS EN EL BANCO: "))
estadoc=input( "ESTADO CIVIL ( C PARA CASADO, S PARA SOLTERO): ")
area=input("ZONA DONDE VIVE( R RURAL , U URBANA : ")
edad= int(2018-year)
if añosbanco >=10 and hijos>=2:
            print("APROBADO")
elif estadoc=="C" and hijos>3 and 45<=year<=55:
            print("APROBADO")
elif ingreso>2500000 and estadoc=="S" and area=="U":
            print("APROBADO")
elif ingreso>3500000 and añosbanco>5:
             print("APROBADO")
elif area=="R" and estadoc=="C" and hijos<2:
             print("APROBADO")
else:
          print("RECHAZADO")