RUT = input("Ingrese Rut :")
suma = sum([ int(a)*int(b)  for a,b in zip(str(RUT).zfill(8), '32765432')])
resultadodigito=11 - (suma %11)
dv = str(resultadodigito)
if resultadodigito == 10:
   dv = 'K'
if resultadodigito == 11:
   dv = '0'
print("dv=" , dv)