#Ordenar tres números
print("ingrese un numero")
n1 = int(input())
print("ingrese un segundo numero")
n2 = int(input())
print("ingrese un tercer numero")
n3 = int(input())


if n2 >= n3 >= n1:
  print(n1,',',n3,',',n2)

elif n1 >= n2 >= n3:
  print(n3,',',n2,',',n1)

elif n2 >= n1 >= n3:
  print(n3,',',n1,',',n2)

elif n2 >= n3 >= n1:
  print(n1,',',n3,',',n2)

elif n3 >= n1 >= n2:
  print(n2,',',n1,',',n3)

elif n3 >= n2 >= n1:
  print(n1,',',n2,',',n3)   