def suma_divisores(a):
  lista = []
  suma = 0
  for i in range(1,a):
    if a%i == 0:
      lista.append(i)
  for i in lista:
    suma = suma+i
  if suma == 1:
    esprimo = True 
  else:  
    esprimo = False
  return(suma,esprimo)
           