i=int(input("Ingreso (en pesos)"))
a=int(input("Año de nacimiento"))
e=2020-a
h=int(input("Número de hijos"))
p=int(input("Años de pertenencia al banco"))
es=str(input("Estado civil (S: soltero, C, casado)"))
v=(str(input("Si vive en campo o cuidad (U: urbano, R: rural)"))
  if p>10 and h>=2:
     print("APROBADO")
  else:
      if es=="C" and h>3 and 45<e<55:
         print("APROBADO")
      else:
           if i>2500000 and es=="S" and v=="U":
             print("APROBADO")
           else:
                if i>3500000 and p>5:
                  print("APROBADO")
                else:
                     if v=="R" and es=="C" and h<2:
                       print("APROBADO")
                     else:
                           print("RECHAZADO")