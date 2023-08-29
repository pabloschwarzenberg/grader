#Ordenar tres números
n1 = int(input("Digite su primer Numero: "))
n2 = int(input("Digite su segundo Numero: "))
n3 = int(input("Digite su tercer Numero: "))
if n1<n2 and n2<n3 or n1==n2 or n2==n1:
  print(n1,",",n2,",",n3)
elif n2<n1 and n1<n3 or n2==n1 or n1==n3:
  print(n2,",",n1,",",n3 )
elif n3<n1 and n1<n2 or n3==n1 or n1==n3:
  print(n3,",",n1,",",n2)
elif n3<n2 and n2<n1 or n3==n2 or n2==n3:
  print(n3,",",n2,",",n1)
elif n1<n3 and n3<n2 or n1==n3 or n3==n2:
  print(n1,",",n3,",",n2)
elif n2<n3 and n3<n1 or n2==n3 or n3==n1:
  print(n2,",",n3,",",n1)