# completa el código de la función
def amigo(a,b):
  for i in range(2,a):
    if(a % i==0):
      b=b+i
  return b
sum1=0
sum2=0
n1=int(input("ingrese primer numero:"))
n2=int(input("ingrese segundo numero:"))
sum1=amigo(n1,sum1)
sum2=amigo(n2,sum2)
if (sum1==n2) and (sum2==n1):
  print("True")
else:
  print("False")
           