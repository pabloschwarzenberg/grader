#Cálculo del dígito verificador de un rut
rut = int(input())
i = 2
suma = 0
while rut:
  digito = rut % 10
  operacion = digito * i
  suma = suma + operacion
  rut //= 10
  print("rut=",rut,"digito=",digito,"operacion=",operacion,"suma=",suma)
  if 7 > i:
    i = i + 1
  else:
    i = 2
  print ("i=",i)
penultimopaso = suma % 11
print (penultimopaso)
dv = 11 - penultimopaso
if dv == 10:
  print ("dv=k")
elif dv == 11:
    print("dv=0")
else:
  print ("dv=",dv)


