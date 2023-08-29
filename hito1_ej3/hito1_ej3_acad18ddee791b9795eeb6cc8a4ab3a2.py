#Aprobación de créditos
a=int(input("Ingrese su ingreso en pesos:$"))
b=int(input("Ingrese su año de nacimiento:"))
c=int(input("Ingrese su número de hijos:"))
d=int(input("Ingrese cantidad de años de pertinencia al banco:"))
e=(input("Ingrese su estado civil 'S': soltero,'C': casado"))
f=(input("Vive en U: urbano,R: rural"))
if(d>10 and c>=2): print ("APROBADO")
else:
   if(e=="C" and c>3 and 45<=(2016-b)<=55): print("APROBADO")
   else:
    if(a>2500000 and e=="S" and f=="U"): print("APROBADO")
    else:
      if(a>3500000 and d>5): print("APROBADO")
      else:
       if(f=="R" and e=="C" and c<2): print("APROBADO")
       else:print("RECHAZADO")
   
