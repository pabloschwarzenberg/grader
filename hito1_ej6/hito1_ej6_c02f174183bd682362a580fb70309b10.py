#Ordenar tres números
#Ordenar tres números

x=int(input('Escriba el primer numero:'))
y=int(input('Escriba el segundo numero:'))
z=int(input('Escriba el tercer numero:'))

if x<y and x<z:
   menor=x
   if  y<z:
       medio,mayor=y,z
   else:
       medio,mayor=z,y
elif y<x and y<z:
   menor=y
   if  x<z:
       medio,mayor=x,z
   else:
       medio,mayor=y,z
else:       
    menor=z
    if  x<y:
       medio,mayor=x,y
    else:
       medio,mayor=z,y  
print("Los números ordenados de menor a mayor son:" + str(menor) + "," + str(medio) + "," + str(mayor))