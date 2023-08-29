#Aprobación de créditos
ing=int(input("Ingreso (en pesos): "))
ann=int(input("Año de nacimiento: "))
nhi=int(input("Número de hijos: "))
anp=int(input("Años de pertenencia al banco: "))
est=input("Estado civil (S: soltero, C, casado): ")
viv=input("Si vive en campo o cuidad (U: urbano, R: rural): ")
anos=2017-ann

if anp>10 and nhi>=2:
    print ("APROBADO")
    
elif est=="C" and nhi>3 and anos>45 and anos<55:    
    print ("APROBADO")
    
elif ing>2500000 and est=="S" and viv=="U":
    print ("APROBADO")

elif viv=="R" and est=="C" and nhi<2:
    print ("APROBADO")
    
else:
    print (" RECHAZADO")        