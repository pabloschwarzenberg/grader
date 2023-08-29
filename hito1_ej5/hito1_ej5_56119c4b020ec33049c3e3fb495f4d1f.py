#Cálculo del dígito verificador de un rut
lista = []
rut = input("Ingrese su RUT sin su digito verificador: ")
for i in rut:
  num = i
  num = int(num)
  lista.append(num)

if len(lista) == 8:
  print(lista)
  lista2 = []
  lista2.append(lista[7]*2)
  lista2.append(lista[6]*3)
  lista2.append(lista[5]*4)
  lista2.append(lista[4]*5)
  lista2.append(lista[3]*6)
  lista2.append(lista[2]*7)
  lista2.append(lista[1]*2)
  lista2.append(lista[0]*3)
  suma = sum(lista2)
  print(suma)

  modulo = suma%11
  resta11 = 11-modulo
  print(resta11)
  dv = 0

  if resta11 == 11:
    dv = 0

  elif resta11 == 10:
    dv = "k"

  else:
    dv = resta11

  print("dv=",dv)

elif len(lista) == 7:
  print(lista)
  lista2 = []
  lista2.append(lista[6]*2)
  lista2.append(lista[5]*3)
  lista2.append(lista[4]*4)
  lista2.append(lista[3]*5)
  lista2.append(lista[2]*6)
  lista2.append(lista[1]*7)
  lista2.append(lista[0]*2)
  suma = sum(lista2)
  print(suma)

  modulo = suma%11
  resta11 = 11-modulo
  print(resta11)
  dv = 0

  if resta11 == 11:
    dv = 0

  elif resta11 == 10:
    dv = "k"

  else:
    dv = resta11

  print("dv=",dv)