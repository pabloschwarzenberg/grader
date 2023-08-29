#Aprobación de créditos
g="APROBADO"
h="RECHAZADO"
z=0
x=0
c=0
v=0
q=int(input(print("ingreso")))
w=int(input(print("año de nacimiento")))
p=2021-w
e=int(input(print("numero de hijos")))
r=int(input(print("años de pertenencia al banco")))
t=(input(print("estado civil (c o s)")))
if(t=="c" or t=="C"):
    z=1
elif(t=="S" or t=="s"):
    x=1
y=input(print("campo o ciudad (u o r)"))
if(y=="u" or y=="U"):
    c=1
if(y=="r" or y=="R"):
    v=1
if(r>=10 and e<=2):
    print(g)
elif(z==1 and e<=3 and p<=45 or p>=55):
    print(g)
elif(q<=2500000 and x==1 and c==1):
    print(g)
elif(q<=3500000 and r>=5):
    print(g)
elif(v==1 and z==1 and e>=2):
    print(g)
else:
    print(h)     