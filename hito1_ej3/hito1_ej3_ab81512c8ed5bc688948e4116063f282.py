#Aprobación de créditos
a=int(input("ingreso(en pesos): "))
b=int(input("año de nacimiento: "))
x=int(input("número de hijos: "))
d=int(input("años de pertenencia al banco: "))
e=input("estado civil (S: soltero, C: casado): ")
f=input("lugar de residencia(U: urbano, R: rural): ")
g=int(2017-b)

if d>10 and x>=2:
  print("APROBADO")
elif e=="C" and x>3 and 44<=b<=45:
  print("APROBADO")
elif a>2500000 and e=="S" and f=="U":
  print("APROBADO")
elif a>3500000 and d>5:
  print("APROBADO")
elif f=="R" and e=="C" and x<2:
  print("APROBADO")
elif false:
  print("RECHAZADO")