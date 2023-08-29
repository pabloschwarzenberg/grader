#Cálculo del dígito verificador de un rut
rut=input()
m=0
s=2
t=0
for i in rut:
  m=eval(i)
  t=t+m*s
  s=s+1
  if s==8:
    s=2
f=int(t/11)
dv=t-(f*11)
print(dv)