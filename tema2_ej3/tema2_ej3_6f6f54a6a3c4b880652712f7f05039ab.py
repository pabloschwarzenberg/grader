def numero_perfecto(a):
    sumas = 0
    divis = a
    x = False
  while divis > 1:
    divis = divis - 1
    if (a % divis) == 0:
        sumas += divis
  if sumas == a:
    x = True
  return x

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           