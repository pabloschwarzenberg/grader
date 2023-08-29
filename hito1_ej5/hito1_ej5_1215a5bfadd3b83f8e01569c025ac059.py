#Cálculo del dígito verificador de un rut
rut=int(input("indique el rut: "))

w=(rut//10000000) * 3
e=((rut//1000000)%10) * 2
r=((rut//100000)%10) * 7
t=((rut//10000)%10) * 6
y=((rut//1000)%10) * 5
u=((rut//100)%10) * 4
i=((rut//10)%10) * 3
o=((rut//1)%10) * 2
adicion=(w+e+r+t+y+u+i+o)
sustraccion1= adicion // 11
sustraccion2=adicion-(11*sustraccion1)
sustraccion=11-sustraccion2
if sustraccion == 11:
    print("dv=",end="")
    print(0)
elif sustraccion == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
print(sustraccion)      