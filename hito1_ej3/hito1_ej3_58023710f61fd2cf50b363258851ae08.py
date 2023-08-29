#Aprobación de créditos
i=int(input("Introduzca su ingreso en pesos: "))
a=int(input("Ingrese su año de nacimiento: "))
h=int(input("¿Cuántos hijos tiene: "))
p=eval(input("Años de pertenencia al banco: "))
e=input("Estado civil: ")
v=input("¿Vive en campo o ciudad?: ")
edad=2020-a

if p>10 and h>=2:
  print("APROBADO")
else:
  if e=="C" and h>3 and 45<=edad<=55:
    print("APROBADO")
  else:
    if i>2500000 and e=="S" and v=="U":
      print("APROBADO")
    else:
      if i>3500000 and p>5:
        print("APROBADO")
      else:
        if v=="R" and e=="C" and h<2:
          print("APROBADO")
        else:
          print("RECHAZADO")      