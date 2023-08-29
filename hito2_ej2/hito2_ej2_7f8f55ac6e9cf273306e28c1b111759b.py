adn=input()
a=list(adn)
for x in range(len(a)):
  palabra=a[x]
  if x=="A" or x=="C" or x=="T" or x=="G" or x=="a" or x=="c" or x=="t" or x=="g":
    x=x+1
  else:
     print("secuencia incorrecta")
     break
  print("Secuencia correcta")
 
  