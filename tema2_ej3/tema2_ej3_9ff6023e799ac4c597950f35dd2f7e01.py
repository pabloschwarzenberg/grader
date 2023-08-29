def numero_perfecto(a):
  n = 1
  s = 0
  es_primo = True
  while n<a:
    if a%n == 0:
      s = s + n
      n = n+1
    elif a%n != 0:
      n = n+1
  if s == a:
    es_primo = True
  elif s != a:
    es_primo = False
  return es_primo
   

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           