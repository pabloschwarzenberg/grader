def amigos(a,b):

  divnumerouno = 1

  divnumerodos = 1

  sumauno = 0

  sumados = 0

  while divnumerouno < a:

    if a%divnumerouno == 0:

      sumauno += divnumerouno

    divnumerouno += 1

  while divnumerodos < b:

    if b%divnumerodos == 0:

      sumados += divnumerodos
     

    divnumerodos += 1

  if sumauno == b and sumados == a:

    return True

  else:

    return False

try:

 numero_1 = int(input("Número 1: "))

 numero_2 = int(input("Número 2: "))

 print(amigos(numero_1,numero_2))

except:

 print("Por favor Ingrese un Número")