#Factores Primos
factor_numero = int(input("ingrese el numero para sacar el factor primo respectivo: "))

asignacion_numero = 2

while asignacion_numero <= factor_numero:

  if factor_numero%asignacion_numero == 0:

    print(asignacion_numero)

    
    
    factor_numero = factor_numero/asignacion_numero

  
  
  else:

    asignacion_numero+=1
      