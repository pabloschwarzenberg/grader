def sistema_ecuaciones(a,b,c,d,e,f):
  det=a*e-b*d
  if det != 0:
    x=(c*e-b*f)/det
    y=(a*f-c*d)/det

    return x,y
  else:
    return None,_None
  print("x=",x,",","y=",y)
