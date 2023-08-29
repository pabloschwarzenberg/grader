def validar(k):
   k=k.upper()
   k=list(k)
   for i in k:
      if (i=="A") or (i=="C") or (i=="T") or (I=="G"):
         k.remove(i)
      if len(k)==0:
         return "correcta"
      else:
         return ("incorrecta")
a=input("ingrese secuencia:")
print(validar(a))