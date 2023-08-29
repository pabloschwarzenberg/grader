a = input("Ingrese secuencia: ") 
def ver(k):
  k = k.upper()
  k = list(k)
  g = k[:]
  for i in k:
      if (i == "A") or (i == "G") or (i == "T") or (i == "C"):
        g.remove(i)
      
      if len(g)  == 0:
        return "correcta"  
       
      elif len(g) != 0:
        return "incorrecta"
        
print(ver(a)) 
          
          