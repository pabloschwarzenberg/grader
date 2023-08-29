a=input()
b=input()
a=list(a)
b=list(b)
n=0
m=[]
for i in range(len(a)):
  if a[i]!=b[n]:
    m.append("_")
  else:
    m.append(b[n])
    n=n+1
for i in range(n,len(b)):
  m.append(b[i])
print("".join(m))
  