#Cálculo del dígito verificador de un rut
dv = int(input("Ingrese su rut para calcularle el digito verificador: "))
# RUT (6  0  0  1  6  7  4  0)
    #  0  1  2  3  4  5  6  7
    # -8 -7 -6 -5 -4 -3 -2 -1
    #  3  2  7  6  5  4  3  2  /Multiplicar todo

if dv > 999999 and dv < 10000000:
  dv = str(dv)
  #Multiplicacion
  a = int(dv[-1])
  m1 = a*2

  b = int(dv[-2])
  m2 = b*3

  c = int(dv[-3])
  m3 = c*4

  d = int(dv[-4])
  m4 = d*5

  e = int(dv[-5])
  m5 = e*6

  f = int(dv[-6])
  m6=f*7

  g = int(dv[-7])
  m7 = g*2

 

  #suma1

  suma1 = m1+m2+m3+m4+m5+m6+m7

  #division

  division1= suma1//11

  #resta

  resta1 = suma1-(11*division1)

  digito_verificador = 11-resta1

  if digito_verificador == 11:
    digito_verificador = 0
    print("dv=", digito_verificador)

  elif digito_verificador == 10:
    digito_verificador = "K"
    print("dv=", digito_verificador)

  else:
    print("dv=", digito_verificador)


elif dv >= 10000000:
  dv= str(dv)
  
  #Multiplicacion
  a = int(dv[-1])
  m1 = a*2

  b = int(dv[-2])
  m2 = b*3

  c = int(dv[-3])
  m3 = c*4

  d = int(dv[-4])
  m4 = d*5

  e = int(dv[-5])
  m5 = e*6

  f = int(dv[-6])
  m6=f*7

  g = int(dv[-7])
  m7 = g*2

  h = int(dv[-8])
  m8 = h*3


  #suma1

  suma1 = m1+m2+m3+m4+m5+m6+m7+m8


  #division

  division1= suma1//11


  #resta

  resta1 = suma1-(11*division1)


  digito_verificador = 11-resta1


  if digito_verificador == 11:
    digito_verificador = 0
    print("dv=", digito_verificador)

  elif digito_verificador == 10:
    digito_verificador = "K"
    print("dv=", digito_verificador)

  else:
    print("dv=", digito_verificador)