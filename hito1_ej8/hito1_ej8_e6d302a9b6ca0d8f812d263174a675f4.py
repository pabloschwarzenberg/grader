#Descomponer un número
n= int(input("Ingrese un numero de hasta 4 digitos:"))
n1= n%10
n= n//10
n2= n%10
n= n//10
n3= n%10
n= n//10
n4= n%10
if (n4!=0):
  print(n4, "M + ", n3, "C + ", n2, "D + ", n1, "U")
elif ((n4==0)and(n3!=0)):
  print(n3, "C + ", n2, "D + ", n1, "U")
elif ((n3==0)and(n4==0)and(n2!=0)):
  print(n2, "D + ", n1, "U")
elif ((n4==0)and(n3==0)and(n2==0)):
  print(n1, "U") 
 