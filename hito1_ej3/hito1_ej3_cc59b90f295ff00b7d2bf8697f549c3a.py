#Aprobación de créditos
i= int(input("Ingreso (en pesos): "))  
y= int(input("Año de nacimiento: "))
h= int(input("Número de hijos: "))
yc= int(input("Años de pertenencia al banco: "))
e= str(input("Estado civil (S: soltero, C: casado): "))
w= str(input("Si vive en campo o cuidad (U: urbano, R: rural): "))
edad = 2021-y

if yc>10 and h>=2:
  print("APROBADO")
elif e=="C" and h>3 and 55>edad>45:
  print("APROBADO")
elif i>2500000 and e =="S" and w=="U":
  print("APROBADO")
elif i>3500000 and yc > 5:
  print("APROBADO")
elif e=="C" and w=="R" and h<2:
  print("APROBADO")
else:
  print("REPROBADO")