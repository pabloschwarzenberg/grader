#Aprobación de créditos
ingreso= int(input("ingrese renta: "))
a_nacimiento= int(input("ingrese fecha de nacimiento: "))
numhijos= int(input("ingrese numero de hijos: "))
a_pertenencia= int(input("ingrese años de pertenecia al banco: "))
e_civil= input("ingrese estado civil S:soltero, C:casado: ")
residencia= input("ingrese si vive en cuidad:U o rural:R ")
if(a_pertenencia>10 and numhijos>2):
    print("APROBADO")
elif(e_civil=="C" and numhijos>3 and (a_nacimiento>=1976 and a_nacimiento<=1966)):
    print("APROBADO")
elif(ingreso>2500000 and e_civil=="S" and residencia=="U"):
    print("APROBADO")
elif(ingreso>3500000 and a_pertenencia>5):
    print("APROBADO")
elif(residencia=="R" and e_civil=="C" and numhijos<2):
    print("APROBADO")
        
       
else:
    print("rechazado")
       

           