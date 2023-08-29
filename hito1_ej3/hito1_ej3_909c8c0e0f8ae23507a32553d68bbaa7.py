#Aprobación de créditos
actual=2017
ingreso=int(input())
nacimiento=int(input())
hijos=int(input())
clientebanco=int(input())
estadocivil=str(input())
campociudad=str(input())
edad=int(2017-nacimiento)
if clientebanco > 10:
   if hijos >= 2:
      print ("APROBADO")
   else:
      print ("RECHAZADO")
else:
   print ("RECHAZADO")
if estadocivil=="C":
   if hijos > 3:
      if 45 <= edad <= 55:
         print ("APROBADO")
      else:
         print ("RECHAZADO")
   else:
      print ("RECHAZADO")
else:
   print ("RECHAZADO")
if ingreso > 2500000:
   if estadocivil=="S":
      if campociudad=="U":
         print ("APROBADO")
      else:
         print ("RECHAZADO")
   else:
      print ("RECHAZADO")
else:
   print ("RECHAZADO")
if ingreso > 3500000:
   if clientebanco > 5:
      print ("APROBADO")
   else:
      print ("RECHAZADO")
else:
   print ("RECHAZADO")
if campociudad=="R":
   if estadocivil=="C":
      if hijos < 2:
         print ("APROBADO")
      else:
         print ("RECHAZADO")
   else:
      print ("RECHAZADO")
else:
   print ("RECHAZADO")
