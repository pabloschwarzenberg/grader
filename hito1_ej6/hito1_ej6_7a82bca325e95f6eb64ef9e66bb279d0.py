#Ordenar tres números
n = input()
n2 = input()
n3 = input()

if n >= n2 >= n3:
  print(n3,",",n2,",",n)
elif n2 >= n >= n3:
  print(n3,",",n,",",n2)
elif n2 >= n3 >= n:
  print(n,",",n3,",",n2)
elif n3 >= n2 >= n:
  print(n,",",n2,",",n3)
elif n3 >= n >= n2:
  print(n2,",",n,",",n3)
elif n >= n3 >= n2:
  print(n2,",",n3,",",n)         