#Ordenar tres números
n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1<n2:
  if n3<n1:
    print(n3,",",n1,",",n2)
  else:
    if n3<n2:
      print(n1,",",n3,",",n2)
    else:
      print(n1,",",n2,",",n3)
else:
  if n3<n2:
    print(n3,",",n2,",",n1)
  else:
    if n3<n1:
      print(n2,",",n3,",",n1)
    else:
      print(n2,",",n1,",",n3)