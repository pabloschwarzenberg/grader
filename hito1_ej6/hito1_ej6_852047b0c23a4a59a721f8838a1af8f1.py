#Ordenar tres números
n1 = input('escriba el numero 1: ')
n2 = input('escriba el numero 2: ')
n3 = input('escriba el numero 3: ')

if n2 < n1 or n3 < n1:
   if n3 > n1:
      print(n2,',',n1,',',n3)
   elif n2 > n1:
      print(n3,',',n1,',',n2)
   elif n2 > n3:
      print(n3,',',n2,',',n1)
   else:
      print(n2,',',n3,',',n1)
else:
   if n2 < n3:
      print(n1,',',n2,',',n3)
   else:
      print(n1,',',n3,',',n2)