#Ordenar tres números
n1=int(input("Ingrese primer numero:"))
n2=int(input("Ingrese segundo numero:"))
n3=int(input("ingrese tercer numero:"))
#proceso
if n1 < n2 and n1 < n3: 
   if n2 < n3: 
     print(n1, ",", n2, ",", n3)
   else:
     print(n1, ",", n3, ",", n2)
elif n2 < n1 and n2 < n3: 
  if n1 < n3:
    print(n2, ",", n1, ",",n3)
  else:
    print(n2, ",", n3, ",", n1)
else:
  if n1<n2:
    print(n3, ",", n1, ",", n2)
  else:
    print(n3, ",", n2, ",", n1)
  
  