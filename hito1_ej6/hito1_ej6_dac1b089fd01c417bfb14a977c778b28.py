#Ordenar tres números
n1=int(input('ingrese cualquier numero:'))
n2=int(input('ingrese cualquier numero:'))
n3=int(input('ingrese cualquier numero:'))
if n1<n2<n3:
  print(n1,n2,n3)
if n1<n3<n2:
  print(n1,n3,n2)
if n2<n1<n3:
  print(n2,n1,n3)
if n2<n3<n1:
  print(n2,n3,n1)
if n3<n2<n1:
  print(n3,n2,n1)
if n3<n1<n2:
  print(N3,N1,N2)