#Factores Primos
def es_primo(numero):
  b=0
  for a in range(2,numero):
      n=numero%a
      if n==0:
         if a!=numero:
            b=b+1
  if b==0 and numero!=1 and numero!=0:
     return(True)
  else:
     return(False)
c=int(input())
for m in range(c):
    if es_primo(m) is True:
        if c%m==0:
            print(m)
if c==2:
    print(2)

      