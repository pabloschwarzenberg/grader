#Aprobación de crédito
ing=int(input("Ingresos mensuales (en pesos):"))
nac=int(input("Edad:"))
hijos=int(input("Numero de hijos:"))
per=int(input("Años de pertenecia al banco:"))
est=str(input("Estado civil(s o c):")) 
vive=input("Vive en campo o ciudad:")

if per>10 ^ hijos>=2:
   print ("APROBADO")
elif est=="c" ^ hijos>3 ^ nac>=45 ^ nac<=55:
   print ("APROBADO")
elif ing>2500000 ^ est=="s" ^ vive==ciudad:
   print ("APROBADO")
elif ing>3500000 ^ per>5:
   print ("APROBADO")
elif vive==campo ^ est=="c" ^ hijos<2:
   print ("APROBADO")
else:
   print ("RECHAZADO")
   