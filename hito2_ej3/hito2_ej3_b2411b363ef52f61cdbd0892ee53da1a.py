a=input()
n=int(input())

l=list(a)
m=[]
s=[]
for i in range(len(a)):
  if i+n>len(a):
    pass
  else:
    m.append(str("".join(l[i:n+i])))
for i in range(len(m)):
  if m.count(m[i])==1:
     s.append(str(m[i]))
  else:
     pass
if len(s)==0:
  print("ninguna")
else:
  print(s)

