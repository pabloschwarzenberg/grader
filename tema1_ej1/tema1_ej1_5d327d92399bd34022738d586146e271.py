#Suma de los N primeros números
print("la suma de los xº primeros números naturales")
x=int(input("ingrese la posición de la suma:"))
s= x*(x + 1)/2
y= abs(x)*(abs(x) + 1)/2#valor absoluto
if x>1:
  print("la suma de los",x,"primeros números naturales es igual a:",s)
else:
  if x<-1:
    print("posición negativa (entera), sin embargo,la corrección es la suma de los",abs(x),"números naturales es:",y)
  else:
    print("los numeros no se pueden sumar")     