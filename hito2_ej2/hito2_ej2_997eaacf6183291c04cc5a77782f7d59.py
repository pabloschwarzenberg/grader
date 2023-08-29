secuencia = input("Ingresa una secuencia: ")
correcta = True
for prot in secuencia:
  if prot.upper() not in 'ACGT':
    print('secuencia incorrecta')
    correcta = False
    break
if correcta == True:
  print('secuencia correcta')