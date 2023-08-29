#Aprobación de créditos
ing= float (input("ingrese su ingreso en pesos:"))
an=float (input ("ingrese su año de nacimiento:"))
nu= float (input ("ingrese cuantos hijos tiene:"))
ab=float (input ("ingrese cuanto años pertenece a este banco:"))
es= input ("ingrese su estado civil S para soltero o C para casado:")
lu=input ("ingrese donde vive R para campo o U para ciudad:")

if ing > 10 and nu >= 2:
          print ("APROBADO")

else:
     print ( "RECHAZADO")
     

if es== "C" and nu > 3 and an <= 1963 and an >= 1973:
    
    print ("APROBADO")
    
else:
    print ("RECHAZADO") 

if ing > 2500000 and es=="S" and lu=="U":
    print ("APROBADO")

else:
    print ("RECHAZADO")

if ing > 3500000 and ab > 5:
    print ("su credito ha sido aprobado")
else:
    print ( "RECHAZADO")

if lu=="R" and es=="C" and nu < 2:
    print ("APROBADO")

else:
    print ("RECHAZADO")
      
      