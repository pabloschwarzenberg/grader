#Aprobación de créditos
i=int(input("Indique su ingreso (en pesos): "))
a=int(input("Ingrese su año de nacimiento: "))
h=int(input("Cantidad de hijos: "))
b=int(input("Años de pertenencia en el banco: "))
e=str(input("Estado civil (conteste con S: soltero, o C: casado): "))
v=str(input("¿Vive en el campo o la ciudad? (Conteste con R: rural, o U: urbano): "))

if(b>10) and(2<=h):
  print("APROBADO")
elif(e=="C") and(3<h) and(45<2017-a<55):
  print("APROBADO")
elif(2500000<i) and(e==str("S")) and(e==str("U")):
  print("APROBADO")
elif(3500000<i) and(5<b):
  print("APROBADO")
elif(v==str("R")) and(h<2):
  print("APROBADO")
else:
  print("RECHAZADO")