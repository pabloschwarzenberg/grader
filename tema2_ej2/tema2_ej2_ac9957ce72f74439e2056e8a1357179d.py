# completa el código de la función
def amigos(a,b):
  amistad = False
  if divisores(a) == b and divisores(b) == a:
    amistad = True
  return amistad

def divisores(num):
  suma = 0
  for i in range(num):
    try:
      if num%(i) == 0:
        suma += (i)
    except:
      dividedByZero = True
  return(suma)
  
#Creí no haber entendido el ejercicio, pero era mi código nomás que no funcionada uwu