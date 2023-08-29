#Cálculo del dígito verificador de un rut
rut = input()

num = rut[::-1]
RUT = range(0,len(rut))
c=0
b=0
for i in RUT :
        a=((i)%6)+2
        b=(a)*(int(num[i]))
        c+=b     
mod11 = c%11
dv=11-mod11
if dv<10 and dv!=0:
        print("dv="+str(dv))
elif dv==10:
        print("dv=K")
else:
        print("dv=0")
