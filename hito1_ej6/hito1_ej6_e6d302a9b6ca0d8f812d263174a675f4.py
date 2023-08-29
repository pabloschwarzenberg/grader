#Ordenar tres números
n1= int(input("Numero 1:"))
n2= int(input("Numero 2:"))
n3= int(input("Numero 3:"))
num=[ n1, n2, n3]
flag=0
num.sort()
for n in num:
  if (flag==0):
    print(n, end="")
    flag=flag+1
  else:
    print(",", n, end="")     