#Cálculo del dígito verificador de un rut
rut = int(input("Mencione su rol unico nacional (run)\n"))
mod = 11

if rut < 9999999 :
  a = rut // 1%10 
  b = rut // 10%10
  c = rut // 100%10
  d = rut // 1000%10
  e = rut // 10000%10
  f = rut // 100000%10
  g = rut // 1000000%10
  codigo = (a * 2) + (b * 3) + (c * 4) + (d * 5) + (e * 6) + (f * 7) + (g * 2)
elif rut > 10000000 : 
  a = rut // 1%10 
  b = rut // 10%10
  c = rut // 100%10
  d = rut // 1000%10
  e = rut // 10000%10
  f = rut // 100000%10
  g = rut // 1000000%10
  h = rut // 10000000%10 
  codigo = (a * 2) + (b * 3) + (c * 4) + (d * 5) + (e * 6) + (f * 7) + (g * 2) + (h * 3) 
  
digito = mod - (codigo - (mod * (codigo // mod))) 
if digito == 11 :
  print("dv=0")
elif digito == 10 :
  print("dv=K")
elif digito < 10 :
  print("dv={}" .format(digito))