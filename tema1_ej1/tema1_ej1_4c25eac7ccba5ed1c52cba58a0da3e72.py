#Suma de los N primeros números
nat=eval(input("Ingrese un numero natural: "))
if nat>0:
  natF=(nat+1)/2
  natF=natF+1+2+3+4
  print("La suma de los" ,nat "primeros números debiera ser", natF)
else:
  print("No es real")