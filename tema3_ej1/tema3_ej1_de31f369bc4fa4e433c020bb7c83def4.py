def suma_divisores(a):
  suma = 0
  for i in range(1,a):
    if a%i == 0:
      suma += i
      
  if suma == 1:
    primo = True
  else:
    primo = False

    
  return(suma, primo)
           