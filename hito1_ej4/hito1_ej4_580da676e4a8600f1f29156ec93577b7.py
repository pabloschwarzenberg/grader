n=eval(input('Ingresar decimal: '))
l=[]
i=1
while n>=1:
  l.append(n%2)
  n = n//2
r=l[::-1]

f=("".join(map(str, r)))
f=eval(f)
print('resultado= ',f)