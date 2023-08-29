print("buen dia estimado cliente")
print("buen dia estimado cliente")
ingresos = eval(input("ingrese sus ingresos en pesos:"))
nacimiento = eval(input("ingrese el año de su nacimiento:"))
añoactual = 2021
edad = (añoactual-nacimiento)
hijos = eval(input("cantidad de hijos:"))
añoscomocliente = eval(input("cuantos años lleva en el banco:"))
estadocivil = input("se encuentra soltero o casado:")
residencia = input("vive en un lugar rural o urbano:")
if (ingresos > 2500000 and estadocivil=="S" and residencia=="U") or (añoscomocliente>10 and hijos>=2) or (estadocivil=="C" and hijos>3 and edad>=45 and edad<=55) or (ingresos>3500000 and añoscomocliente>5) or (residencia=="R" and estadocivil=="C" and hijos<2) :
  print("APROBADO")
else:
  print("RECHAZADO")