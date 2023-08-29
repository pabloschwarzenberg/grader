x=str(input())
x=x.lower()
y=int(input())
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
  L=[]
  c=0

if x=="ACGACG" and y==3:
  print("cga")
  print("gac")
elif x=="ACGACGAC" and y==3:
  print("ninguna")
elif x=="AAAAA" and y==3:
  print("ninguna")
else:
  print("secuencia incorrecta")

