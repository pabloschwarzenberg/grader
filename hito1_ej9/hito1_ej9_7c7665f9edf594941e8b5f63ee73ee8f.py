def Ecuacion(a,b,c,d,e,f):
  y = (c * d + f * -a) / (b * d + e * -a)
  x = f - e * ((c * d + f * -a) / (b * d + e * -a))
  return x, y
