#Ordenar tres números
n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

while True:
  if n1 <= n2 and n2 <= n3:
    print("{0},{1},{2}".format(n1, n2, n3))
    break
  
  else:
    if n1 >= n2:
      n1, n2 = n2, n1
     
    elif n2 >= n3:
      n2, n3 = n3, n2