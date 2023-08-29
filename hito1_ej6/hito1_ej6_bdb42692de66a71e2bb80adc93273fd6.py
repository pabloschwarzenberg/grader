#dhariel portocarrero
#hito 1 3 numeros enteros ordenados de menor a mayor
print("ingresa 3 numeros que los ordenare de menor a mayor")
n1=int(input("ingrese un primer numero : "))
n2=int(input("ingrese un segundo numero: "))
n3=int(input("ingrese un tercer numero: "))
if ((n1 < n2) and (n2 < n3) and (n1 < n3)):
 print(n1, ",", n2, ",", n3)
if ((n2 < n1) and (n1 < n3) and (n2 < n3)):
 print(n2, ",", n1, ",", n3)
if ((n3 < n1) and (n1 < n2) and (n3 < n2)):
 print(n3, ",", n1, ",", n2)
if ((n3 < n2) and (n2 < n1) and (n3 < n1)):
 print(n3, ",", n2, ",", n1)
if ((n2 < n3) and (n3 < n1) and (n2 < n1)):
 print(n2, ",", n3, ",", n1)
if ((n1 < n3) and (n3 < n2) and (n1 < n2)):
 print(n1, ",", n3, ",", n2)
if (n1 == n2 == n3):
 print(n1, ",", n2, ",", n3)
if(n1==n2)and(n1<n3):
  print(n1,",",n2,",",n3)
if(n2==n3)and(n2<n1):
  print(n2,",",n3,",",n1)
if(n1==n3)and(n1<n2):
  print(n1,",",n3,",",n2)
if(n1==n2)and(n1>n3):
  print(n3,",",n2,",",n1)
if(n2==n3)and(n2>n1):
  print(n1,",",n3,",",n2)
if(n1==n3)and(n1>n2):
  print(n2,",",n3,",",n1)