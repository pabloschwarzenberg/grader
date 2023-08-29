#Aprobación de créditos
I=int(input("Ingreso en pesos ($):"))
agno=int(input("Año de nacimiento:"))
n=int(input("Número de hijos:"))    
Agno=int(input("Años pertenecientes al banco:"))
E=input("Estado civil (S:Soltero / C:Casado:)")

while(E!= "S" and E!="s" and E!="c" and E!="C"):
    E=input("Debe ingresar (S:Soltero / C:Casado):")
    
Z=input("Zona rural o urbana (R:Rural / U:Urbana):")
while(Z!= "U" and Z!="u" and Z!="R" and Z!="r"):
    Z=input("Debe ingresar (R Rural / U Urbana):")
           
#Si el cliente pertenece más de 10 años al banco, y tiene dos o más hijos.
if(Agno>10 and n >1):
   print("APROBADO")
#Si el cliente es casado, tiene más de tres hijos, y tiene entre 45 y 55 años.
elif ((E=="C" or E=="c")) and n >3 and (agno <1973 and agno >1961):
   print("APROBADO")
#Si el cliente posee ingresos superiores a $2.500.000, es soltero y vive en la ciudad.
elif ((I>2500000) and (E=="S" or E=="s") and (Z=="U" or Z=="u")):
   print("APROBADO")
#Si el ciente tiene ingresos superiores a $3.500.000 y pertenece al banco por más de 5 años
elif ((I>3500000) and (Agno>5)):
   print("APROBADO")
#Si el cliente vive en el campo, es casado y tiene menos de dos hijos.
elif ((Z=="R" or Z=="r") and (E=="C" or E=="c") and (n<2)):
   print("APROBADO")
# De lo contrario se rechazo el credito
else :print("RECHAZADO")
                 