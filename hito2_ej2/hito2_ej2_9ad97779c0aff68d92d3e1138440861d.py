m=input("Escriba su posible secuencia de geneoma")
i=0
m=m.upper()

while i<len(m):
  if m[i]=="A" or m[i]=="T"or m[i]=="G"or m[i]=="C":
    i=i+1
    if i==len(m)-1:
        print("Secuencia correcta")
  else:
    print("Secuencia incorrecta")
    break
    
    