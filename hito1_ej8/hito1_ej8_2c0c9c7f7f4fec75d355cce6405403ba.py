#Descomponer un número
n=int(input())
m=(n%10000)//1000
c=(n%1000)//100
d=(n%100)//10
u=(n%10)
r=[]
if n>999 and n<10000:
  r.append(str(m))
  r.append("M + ")
  r.append(str(c))
  r.append("C + ")
  r.append(str(d))
  r.append("D + ")
  r.append(str(u))
  r.append("U")
if n>99 and n<1000:
  r.append(str(c))
  r.append("C + ")
  r.append(str(d))
  r.append("D + ")
  r.append(str(u))
  r.append("U")
if n>9 and n<100:
  r.append(str(d))
  r.append("D + ")
  r.append(str(u))
  r.append("U")
if n>0 and n<10:
  r.append(str(u))
  r.append("U")    
r=''.join(r)
print(r)      