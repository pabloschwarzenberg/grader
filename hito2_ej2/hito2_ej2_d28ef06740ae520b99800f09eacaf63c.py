def adn(x):
  count=0  
  for i in range (0,len(x)):
    if i=="a" or i=="A" or i=="c" or i=="C" or i=="T" or i=="t" or i=="G" or i=="g":
      pass
    else:
      count+=1
    if count == 0:
      return "correcta"
    else:
      return "incorrecta"
      
a = str(input("Ingrese secuencia:"))
print (adn(a))