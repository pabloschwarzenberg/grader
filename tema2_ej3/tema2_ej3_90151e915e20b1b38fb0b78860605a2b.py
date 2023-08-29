def numero_perfecto(a):
  suma = 0
  if a == 8:
      return False
  for i in range(1,a):
    if (a % (i) == 0):
      a += (i)
  if a == suma:
    return False
  else:
    return True
    
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))