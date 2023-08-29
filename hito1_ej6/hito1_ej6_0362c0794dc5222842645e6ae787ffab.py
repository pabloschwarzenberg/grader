#Ordenar tres números
N1 = eval(input())
N2 = eval(input())
N3 = eval(input())
n1 = N1
n2 = N2
n3 = N3
if(N1 >= N2 >= N3):
  print("{}, {}, {}". format(N3,N2,N1))
if(N1 <= N2<= N3):
  print("{},{},{}". format(N1,N2,N3))
if(N1 >= N3 >= N2):
    print("{},{},{}". format(N2,N3,N1))
if(N1 <= N3 <= N2):
    print("{},{},{}". format(n1,n3,n2))
if(n2 >= n1 >= n3):
    print("{},{},{}". format(n3,n1,n2))
if(n2 <= n1 <= n3):
    print("{},{},{}". format(n2,n1,n3))
if(n2 >= n3 >= n1):
    print("{},{},{}". format(n1,n3,n2))
if(n2 <= n3 <= n1):
    print("{},{},{}". format(n2,n3,n1))
if(n3 >= n1 >= n2):
    print("{},{},{}". format(n2,n1,n3))
if(n3 <= n1 <= n2):
    print("{},{},{}". format(n3,n1,n2))
if (n3 >= n2 >= n1):
    print("{},{},{}".format(n1, n2, n3))
if(n3 <= n2 <= n1):
    print("{},{},{}". format(n3,n2,n1))

