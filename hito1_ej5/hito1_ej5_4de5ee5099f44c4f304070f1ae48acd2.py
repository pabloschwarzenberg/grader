#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut:"))
s=(rut//10000000) * 3
t=((rut//1000000)%10) * 2
h=((rut//100000)%10) * 7
o=((rut//10000)%10) * 6
l=((rut//1000)%10) * 5
e=((rut//100)%10) * 4
q=((rut//10)%10) * 3
w=((rut//1)%10) * 2
s=(s+t+h+o+l+e+q+w)
m1= s // 11
m2= s-(11*m1)
m=11-m2
if(m == 11):
    print("dv=",end="")
    print(0)
elif(m == 10):
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(m)