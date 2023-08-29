#Ordenar tres números
E=int(input("ingrese numero 1 : "))
F=int(input("ingrese numero 2 : "))
G=int(input("ingrese numero 3 : "))
if(E<=F<=G):
  print(str(E)+","+str(F)+","+str(G))
elif(E<=G<=F):  
  print(str(E)+","+str(G)+","+str(F))
elif(F<=E<=G):  
  print(str(F)+","+str(E)+","+str(G))
elif(F<=G<=E):  
  print(str(F)+","+str(G)+","+str(E))
elif(G<=E<=F):  
  print(str(G)+","+str(E)+","+str(F))
elif(G<=F<=E):  
  print(str(G)+","+str(F)+","+str(E))  