#Ordenar tres números
#Entrada
n1 = int(input("Ingrese su primer numero: "))
n2 = int(input("Ingrese su segundo numero: "))
n3 = int(input("Ingrese su tercer numero: "))

#operatoria
if n1<=n2<=n3:
  print(n1, ",", n2, ",", n3)
elif n1<=n3<=n2:
  print(n1, ",", n3, ",", n2)
elif n2<=n3<=n1:
  print(n2, ",", n3, ",", n1)
elif n2<=n1<=n3:
  print(n2, ",", n1, ",", n3)
elif n3<=n1<=n2:
  print(n3, ",", n1, ",", n2)
elif n3<=n2<=n1:
  print(n3, ",", n2, ",", n1)
  

else:
  print("Su datos son invalidos")
      
