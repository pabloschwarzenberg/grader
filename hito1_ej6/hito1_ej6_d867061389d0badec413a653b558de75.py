#Ordenar tres números
m=int(input("Ingrese un número: "))
n=int(input("Ingrese otro número: "))
p=int(input("Ingrese otro número: "))
if m<=n<=p :
  print(m,",",n,",",p)
elif m<=p<=n :
    print(m,",",p,",",n)
elif n<=m<=p :
  print(n,",",m,",",p)
elif n<=p<=m :
  print(n,",",p,",",m)
elif p<=m<=n :
  print(p,",",m,",",n)
else :
  print(p,",",n,",",m)