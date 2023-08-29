#Ordenar tres números
n1=int(input())
n2=int(input())
n3=int(input())
if n1<=n2 and n2<=n3:
  print("{},{},{}".format(n1,n2,n3))
elif n1<=n3 and n3<=n2:
  print("{},{},{}".format(n1,n3,n2))
elif n2<=n3 and n3<=n1:
  print("{},{},{}".format(n2,n3,n1))
elif n2<=n1 and n1<=n3:
  print("{},{},{}".format(n2,n1,n3))
elif n3<=n1 and n1<=n2:
  print("{},{},{}".format(n3,n1,n2))
elif n3<=n2 and n2<=n1:
  print("{},{},{}".format(n3,n2,n1))
  