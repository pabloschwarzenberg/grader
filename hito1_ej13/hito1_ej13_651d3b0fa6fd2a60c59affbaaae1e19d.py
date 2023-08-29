def es_primo(b):
    c=0
    z=0
    while (c<b):
        c=c+1
        if(b%c==0):
            z=z+1;
    if(b==1 or b==0):
      z=3
    if(z<=2):
        return(True)
    else:
        return(False)
a=int(input())
i=2
while i<=a:
  if a%i==0:
    if es_primo(i)==True:
      print(i)
  i=i+1