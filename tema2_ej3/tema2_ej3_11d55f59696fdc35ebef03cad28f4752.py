def numero_perfecto(a):
  x = a
  z = 0
  for y in range(x-1):
    c = x % (y+1)
    if c == 0:
      z += (y+1)
  if z == a:
    return True
  else:
    return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           