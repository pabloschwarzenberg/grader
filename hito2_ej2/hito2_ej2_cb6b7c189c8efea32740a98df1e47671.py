x=str(input())
x=x.lower()
n=0
l=0
while n<len(x) :
  if x[n]=="a" :
    n=n+1
  elif x[n]=="c" :
    n=n+1
  elif x[n]=="t" :
    n=n+1
  elif x[n]=="g" :
    n=n+1
  else :
    l=l+1
    break
if l==0 :
  print("secuencia correcta")
else:
  print("secuencia incorrecta")
   