#Descomponer un número
#Escribe un programa que le pida al usuario un número de hasta 4 dígitos y que te entregue la descomposición en Unidades, Decenas, Centenas y Miles. 
numero=int(input("Ingrese un número de hasta 4 dígitos: "))
n4=int(numero%10)
n1=int(numero//1000)
n2=int(numero//100)%10
n3=int(numero%100)//10
if n1>0:
  print(n1,"M +",n2,"C +",n3,"D +",n4,"U")
elif n1==0 and n2>0:
  print(n2,"C +",n3,"D +",n4,"U")
elif n1==0 and n2==0 and n3>0:
  print(n3,"D +",n4,"U")
elif n1==0 and n2==0 and n3==0 and n4>0:
  print(n4,"U")