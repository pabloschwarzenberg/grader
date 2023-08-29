#Aprobación de créditos
Ingreso = int(input("ingrese sus ingresos uwu"))
Nacimiento = int(input("ingrese su año de nacimiento"))
Hijos =  int(input("ingrese le cantided de hijes"))
AB =  int(input(" ingrese el numero de años que ha estado estado en el banco"))
Civil =  input("ingrese S si esta soltero, ingrese C si esta casade")
Entorno = input(" ingrese U para urbano ingrese R para rural")

Edad = 2022 - Nacimiento 

aprovado = False 
if AB > 10 and Hijos >= 2:
  aprovado = True 

if Civil == "C" and Hijos > 3 and  Edad >=45 and Edad <=55:
  aprovado = True
 
if Ingreso >2500000 and Civil == "S" and Entorno == "U": 
  aprovado = True 
  
if Ingreso > 3500000 and AB > 5: 
  aprovado = True 
  
if Entorno == "R" and Civil == "C" and Hijos < 2: 
  aprovado = True 
  
if aprovado == True:
  print("APROBADO")
  
else:
  print ("RECHAZADO")    

