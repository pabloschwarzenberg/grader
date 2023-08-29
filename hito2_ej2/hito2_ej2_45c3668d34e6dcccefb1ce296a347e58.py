s=str(input("secuencia"))
s=s.upper()
b=len(s)
contador=0
for m in s:
    if m=="A" or m=="C" or m=="T" or m=="G":
        contador=contador+1
if contador==b:
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
      