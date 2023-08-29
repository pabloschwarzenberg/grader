# completa el código de la función
def suma_divisores(a):
  n = 1
  s = 0
  es_primo = True
  while n<a:
    if a%n == 0:
      s = s + n
      n = n+1
    elif a%n != 0:
      n = n+1
  if s == 1:
    es_primo = True
  elif s != 1:
    es_primo = False
  return s,es_primo
           