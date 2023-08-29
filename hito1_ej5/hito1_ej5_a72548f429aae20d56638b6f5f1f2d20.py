#Cálculo del dígito verificador de un rut
rut = eval(input("Ingrese dígitos del rut"))
uno = rut // 10000000
rut = rut % 10000000
dos = rut // 1000000
rut = rut % 1000000
tres = rut // 100000
rut = rut % 100000
cuatro = rut // 10000
rut = rut % 10000
cinco = rut // 1000
rut = rut % 1000
seis = rut // 100
rut = rut % 100
siete = rut // 10
rut = rut % 10
ocho = rut // 1
rut = rut % 1
resultado = ((uno * 3) + (dos * 2) + (tres * 7) + (cuatro * 6) + (cinco * 5) + (seis * 4) + (siete * 3) + (ocho * 2))
res_dos = resultado // 11
res_tres = (resultado - (11 * res_dos))
res_final = 11 - res_tres
if(res_final == 11):
  print("dv=0")
elif(res_final == 10):
  print("dv=K")
else:
  print("dv=", res_final)