#Ordenar tres números
n1=eval(input("primer numero:"))
n2=eval(input("segundo numero:"))
n3=eval(input("tercer numero:"))

b = min(n1,n2,n3)

if n1 == b:
  if n2 <= n3:
    print(b,",",n2,",",n3)
  else:
    print(b,",",n3,",",n2)

elif n2 == b:
  if n1 <= n3:
    print(b,",",n1,",",n3)
  else:
    print(b,",",n3,",",n1)

else:
  if n1 <= n2:
    print(b,",",n1,",",n2)
  else:
    print(b,",",n2,",",n1)