#Descomponer un número
n=int(input())
while True:
  if n<10:
    n=str(n)
    n1=n[-1]
    print(n1,"U")
    break
  if n<100:
    n=str(n)
    n1=n[-1]
    n2=n[-2]
    print(n2,"D +",n1,"U")
    break
  if n<1000:
    n=str(n)
    n1=n[-1]
    n2=n[-2]
    n3=n[-3]
    print(n3,"C +",n2,"D +",n1,"U")
    break
  if n<10000:
    n=str(n)
    n1=n[-1]
    n2=n[-2]
    n3=n[-3]
    n4=n[-4]
    print(n4,"M +",n3,"C +",n2,"D +",n1,"U")
    break