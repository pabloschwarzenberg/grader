secuencia=input("Inserte secuencia a validar:")
lista_s=list(secuencia)
suma=0
for i in list(secuencia):
  if i=="A" or i=="C" or i=="T" or i=="G" or i=="a" or i=="c" or i=="t" or i=="g":
      suma+=1
if suma==len(secuencia):
    print("Secuencia correcta")
else:
    print("Secuencia incorrecta")
