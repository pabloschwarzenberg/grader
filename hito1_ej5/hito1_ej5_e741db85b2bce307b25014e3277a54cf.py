#Cálculo del dígito verificador de un rut
rut=input()
if len (rut)==7:
  rut="0"+rut
a=rut[0]
b=rut[1]
c=rut[2]
d=rut[3]
e=rut[4]
f=rut[5]
g=rut[6]
h=rut[7]

i=int(a)*3
j=int(b)*2
k=int(c)*7
l=int(d)*6
m=int(e)*5
n=int(f)*4
o=int(g)*3
p=int(h)*2


o=i+j+k+l+m+n+o+p
resto=(o%11)
q=(11-resto)

if(q==10):
  print("dv=k")
 
elif(q==11):
    print("dv=0")
else:
    print("dv=",q)

