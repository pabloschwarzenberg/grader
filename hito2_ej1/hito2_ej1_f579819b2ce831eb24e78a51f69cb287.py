a=input()
b=input()
a=list(a)
b=list(b)
n=0
c=[]
for i in range(0, len(a)):
  if a[i]!=b[n]:
    c.append("_")
  else:
    c.append(b[n])
    n=n+1
for i in range(n,len(b)):
  c.append(b[i])
print("".join(c))
  