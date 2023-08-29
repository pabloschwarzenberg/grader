secuencia = input()
secuencia = secuencia.upper()
validez = True
for i in range(len(secuencia)):
  if secuencia[i] in ' ACTG ':
    validez = True
  elif secuencia[i] not in ' ACTG ':
    validez = False
    break
if validez == True:
  print('secuencia correcta')
elif validez == False:
  print('secuencia incorrecta')