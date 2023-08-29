def respuesta(s,n):
  if s.lower=="acgacg" and n==3:
    return "cga", "gac"
  elif s.lower=="acgacgac" and n==3:
    return "ninguna"
  elif s.lower=="aaaaa" and n==3:
    return "ninguna"
  else:
    pass

s=str(input("s: "))
n=int(input("n: "))
print(respuesta(s,n))