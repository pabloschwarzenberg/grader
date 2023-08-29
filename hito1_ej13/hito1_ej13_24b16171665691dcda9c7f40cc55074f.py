#Factores Primos
def es_primo(o):
  x=0
  for k in range(2,o):
      numero =o%k
      if numero ==0:
         if k!=o:
            x=x+1
  if x==0 and o!=1 and o!=0:
     return(True)
  else:
     return(False)
u =int(input())
for ma in range(u):
    if es_primo(ma) is True:
        if u%ma==0:
            print(ma)
if u==2:
    print(2)
