#Cálculo del dígito verificador de un rut

r = input("Ingrese su rut sin el guion")
a = len(r)

t = 2*int(r[-1])
t = t + 3*int(r[-2])
t = t + 4*int(r[-3])
t = t + 5*int(r[-4])
t = t + 6*int(r[-5])
t = t + 7*int(r[-6])
t = t + 2*int(r[-7])
if a == 8:
  t = t + 3*int(r[-8])
resto = t % 11
digito = 11 - resto
if digito == 11:
  print("dv=0")
elif digito == 10:
  print("dv=k")
else:
  print("dv=",digito)     