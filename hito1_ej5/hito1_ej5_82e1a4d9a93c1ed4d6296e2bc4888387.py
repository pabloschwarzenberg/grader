#Cálculo del dígito verificador de un rut
rut_texto = input('Ingrese un RUT: ')

recorrido = len(rut_texto)
rut = int(rut_texto)
suma_prod = 0
mult = 2

print()
for i in range(recorrido):
  
  digito = rut % 10
  suma_prod += digito * mult
  rut = rut // 10
  if mult == 7:
    mult = 2
  else:
    mult += 1

resto_suma_prod = suma_prod % 11

if 11-resto_suma_prod == 11:
  dv = 0
elif 11-resto_suma_prod == 10:
  dv = 'k'
else:
  dv = 11-resto_suma_prod

print()
print('dv=', dv, sep='') 
