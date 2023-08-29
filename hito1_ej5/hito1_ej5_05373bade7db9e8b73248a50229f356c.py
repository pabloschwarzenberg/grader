#Cálculo del dígito verificador de un rut
rut=int(input())
a=rut-(rut//10)*10
b=(rut-(rut//100)*100-a)//10
c=(rut-(rut//1000)*1000-b*10-a)//100
d=(rut-(rut//10000)*10000-c*100-b*10-a)//1000
e=(rut-(rut//100000)*100000-d*1000-c*100-b*10-a)//10000
f=(rut-(rut//1000000)*1000000-e*10000-d*1000-c*100-b*10-a)//100000
g=(rut-(rut//10000000)*10000000-f*100000-e*10000-d*1000-c*100-b*10-a)//1000000
h=(rut-(rut//100000000)*100000000-g*1000000-f*100000-e*10000-d*1000-c*100-b*10-a)//10000000
s=a*2+b*3+c*4+d*5+e*6+f*7+g*2+h*3
r=(s%11)
rr=11-r
if rr==11:
    print("dv=0")
elif rr==10:
    print("dv=K")
else:
    print("dv=",rr)