a = input("Ingrese secuencia: ")
def ver(k):
  k = k.upper()
  k = list(k)
  g = k[:]
  for i in k:
    if (i == "A") or (i == "C") or (i == "T") or (i == "G"):
      g.remove(i)
    
    if len(g) == 0:
      return "correcta"
      
    else:
      return "incorrecta"
      
print(ver(a))


