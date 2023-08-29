import datetime 
ingreso=int(input("ingrese el total de sus Ingreso (en pesos):"))
añoNacimiento=int(input("ingrese el año de su nacimiento:"))
nHijo=int(input("ingrese n° de hijos:"))
añosPertenencia=int(input("años de pertenencia:"))
eCivil=input("ingrese S si es soltero o C si es casado:")
vive=input("si vive en campo ingrese R, si vive en cuidad ingrese U:")
hoy=datetime.date.today()
añoActual=int(hoy.strftime('%Y'))
edad=(añoActual-añoNacimiento)
print (añoActual)
print (edad)

#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if (añosPertenencia>10) and (nHijo>=2):
         print ("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.        
elif (eCivil=="C" or eCivil=="c") and  (nHijo>3) and (edad>=45) and (edad <=55) :
         print ("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif (ingreso>2500000) and (eCivil=="S" or eCivil=="s" ) and (vive=="U" or vive=="u"):
         print ("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif (ingreso>3500000) and (añosPertenencia>5):
         print ("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif(vive=="R" or vive=="r") and (eCivil=="C" or eCivil=="c" ) and (nHijo<2):
        print ("APROBADO")
else:
         print ("RECHAZADO") 
