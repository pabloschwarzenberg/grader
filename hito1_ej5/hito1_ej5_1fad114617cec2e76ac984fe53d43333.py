rut=int(input("rut"))
a=rut//10000000
b=(rut//1000000)-a*10
c=(rut//100000)-(a*10+b)*10
d=(rut//10000)-(a*100+b*10+c)*10
e=(rut//1000)-(a*1000+b*100+c*10+d)*10
f=(rut//100)-(a*10000+b*1000+c*100+d*10+e)*10
g=(rut//10)-(a*100000+b*10000+c*1000+d*100+e*10+f)*10
h=(rut//1)-(a*1000000+b*100000+c*10000+d*1000+e*100+f*10+g)*10
suma=a*8+b*9+c*4+d*5+e*6+f*7+g*8+h*9
resto=suma%11
if resto==10:
    print("dv=k")
else:
    print("dv="+str(resto))


      