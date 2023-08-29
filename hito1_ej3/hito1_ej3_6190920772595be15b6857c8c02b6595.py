#Aprobación de créditos
print("le haremos unas preguntas para verificar si aprueba o no el credito ")
ingresos= int(input("cual es su ingreso en pesos "))
ano_nacimiento= int(input("su año de nacimiento "))
if(ano_nacimiento>2021):
    print("seleccione un año coherente, corra el programa de nuevo")
edad=(2021-(ano_nacimiento))
nhijos= int(input("cuantos hijos tiene, si no tiene ponga 0 "))
if(nhijos<0):
    print("Ingrese un numero coherente")
anos_banco= int(input("cuantos anos lleva perteneciendo al banco "))
if(anos_banco<0):
    print("Ingrese un ano correcto")
casado="casado"
soltero="soltero"
estado_civil= input("su estado civil casado o soltero? ")
ec=estado_civil.lower()

rural="rural"
urbana="urbana"
residencia= input("Ustes vive en zona rural o urbana ")
if(residencia!= rural) and (residencia!= urbana):
  print("porfavor, escriba lo que se le pidio")
   
if(anos_banco>10) and (nhijos>2):
    print("APROBADO")
if(estado_civil==casado) and (nhijos>3) and (edad>=45) and (edad<=55):
    Print("APROBADO")
if(ingresos>2500000) and (ec==soltero) and (residencia==rural):
    print("APROBADO")
if(ingresos>3500000) and (anos_banco>5):
    print("APROBADO")
if(residencia==rural) and (ec==casado) and (nhijos<2):
    print("APROBADO")
else:
    print("NO APRUEBA")



    print("APROBADO")
if(residencia==rural) and (ec==casado) and (nhijos<2):
    print("APROBADO")
else:
    print("NO APRUEBA")
   




    