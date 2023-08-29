def numero_perfecto(a):
  n = 0
  for i in range (1,a):
    if a%i == 0:
      n = n+i
    else:
      continue
  if n == a:
    return True
  else:
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           