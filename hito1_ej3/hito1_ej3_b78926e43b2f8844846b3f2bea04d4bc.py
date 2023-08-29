#Aprobación de créditos
a=int(input("Introduzca su ingreso(en pesos): "))
b=int(input("Introduzca su año de nacimiento: "))
c=int(input("Introduzca su número de hijos: "))
d=int(input("Cantidad de años de pertenencia al banco: "))
e=(input("Estado civil: S (soltero), C (casado) "))
f=(input("¿Dónde vive? U (urbano), R (rural) "))
g= 2016-b
if e!="S" and e!= "C":
     print("Error: Se ha ingresado el estado civil de manera incorrecta.")
elif f!="U" and f!="R":
        print("Error: Se ha ingresado el su localidad de manera incorrecta.")
elif d>10 and c>=2:
         print("APROBADO")
elif e=="C" and c>3 and 55>g>45:
          print("APROBADO")
elif a>2500000 and e =="S" and f==1:
      print("APROBADO")
elif a>3500000 and d>5:
      print ("APROBADO")
elif f=="R" and e=="C" and c<=2:
      print ("APROBADO")
else:
      print ("RECHAZADO")    