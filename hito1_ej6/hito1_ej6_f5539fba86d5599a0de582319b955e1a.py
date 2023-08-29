#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
s=0
if a>=b and a>=c: 
     if b>=c:
        s=c,b,a
     else:
        s=b,c,a
elif b>=a and b>=c:
      if a>=c:
        s=c,a,b
      else: 
        s=a,c,b
else:
      if a>=b:
        s=b,a,c
      else:
        s=a,b,c
print(s)  