s=input()
n=int(input())
l=list(s)
t = []
f =[]
for i in range(0,len(l)):
  while i <= len(l)-n:
    t.append("".join(l[i:i+n]))
    break
for i in range(len(t)):
  if t.count(t[i]) == 1:
    f.append(str(t[i]))
  else:
    continue
if len(f)==0:
  print("ninguna")
else:
  print(f)