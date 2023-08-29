def numero_perfecto(a):
  resultado = [ i for i in range(1, a + 1) if a % i == 0]
  resultado.remove(a)
  suma = 0
  for elemento in resultado:
   suma += elemento
 
  if suma == a:
      perfecto = True
  else:
      perfecto = False

  return perfecto


