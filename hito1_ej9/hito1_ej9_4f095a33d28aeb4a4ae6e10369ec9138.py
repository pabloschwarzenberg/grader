#Sistema de Ecuaciones
while True:
  print("Asigne valores a a,b,c,d,e y f")
  print("ax+by=c")
  print("dx+ey=f")
  a = float(input("a: "))
  b = float(input("b: "))
  c = float(input("c: "))
  d = float(input("d: "))
  e = float(input("e: "))
  f = float(input("f: "))
  print(a,"x", "+" , b,"y" , "=" , c)
  print(d,"x", "+" , e,"y" , "=" , f)
  if (b*d - a*e)==0 or a==0:
    print("El sistema no tiene solución")

  else:
    y = (c*d - a*f)/(b*d - a*e)
    x = (c - b*y)/a
    print("x = ", x)
    print("y = ", y)

  print("\n")

  break
      