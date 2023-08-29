#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut:"))

q=(rut//10000000)*3
w=((rut//1000000)%10)*2
e=((rut//100000)%10)*7
r=((rut//10000)%10)*6
t=((rut//1000)%10)*5
y=((rut//100)%10)*4
u=((rut//10)%10)*3
i=((rut//1)%10)*2

suma=(q+w+e+r+t+y+u+i)
resto=(suma//11)
resto_r=(suma-(11*resto))
final=(11-resto_r)

if final==11:
    print("dv=0")
else:
    if final==10:
        print("dv=K")

    if (final!=11)or(final!=10):
        print("dv=",final)