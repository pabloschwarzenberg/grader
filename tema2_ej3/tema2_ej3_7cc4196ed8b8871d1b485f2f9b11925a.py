def numero_perfecto(n):
  c=1
  s=0
  while c != n:
    if n%c == 0:
      s = s+c
    c = c + 1
  if s == n:
    return True
  else:
    return False

if __name__=="__main__":
  n = eval(input("Ingrese su numero"))
  if numero_perfecto(n):
    print("El numero {0} es perfecto".format(n))
  else:
    print("El numero {0} no es perfecto".format(n)) 