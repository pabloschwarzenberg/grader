def suma_divisores(a):
  suma = 0
  for i in range(1, a):
    print(i)
    if a % i == 0:
      suma += i
    
  es_primo = suma == 1
    
  return (suma, es_primo)