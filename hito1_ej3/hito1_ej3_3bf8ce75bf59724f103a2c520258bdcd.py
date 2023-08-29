#Aprobación de créditos
p=eval(input("Ingrese sus ingresos que tiene en clp:$"))
a=eval(input("Ingrese su año de nacimiento:"))
n=eval(input("Ingrese el número de hijos o hijas que tiene:"))
ab=eval(input("Ingrese los años que ha estado en el banco:"))
ec=input("Ingrese si está soltero o casado:")
S="soltero"
C="casado"
v=input("Ingrese si vive en estado urbano o rural:")
U="urbano"
R="rural"
if ab>10 and n>=2:
  print("APROBADO")
elif ec==C and n>3 and 1965<=a<=1975:
  print("APROBADO")
elif p>1500000 and ec==S and v==U:
  print("APROBADO")
elif p>3500000 and ab>5:
  print("APROBADO")
elif ec==C and v==R and n<2:
  print("APROBADO")
else:
  print("RECHAZADO")