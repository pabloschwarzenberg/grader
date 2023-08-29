#Cálculo del dígito verificador de un rut
rut = str(input("ingrese un rut sin digito verificador :"))

serie = "234567"
p_rut = len(rut)-1
p_serie = 0
suma = 0
while p_rut >= 0:
  if p_serie == len(serie):
    p_serie = 0
  multiplicacion = int(rut[p_rut])*int(serie[p_serie])
  suma = suma + multiplicacion
  p_rut = p_rut - 1
  p_serie = p_serie + 1

modulo11 = 11 - (suma % 11)
if modulo11 == 11:
  dv = 0
elif modulo11 == 10:
  dv = "K"
else:
  dv = modulo11

print("dv=",dv)