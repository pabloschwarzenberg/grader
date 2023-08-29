a=int(input("rut:"))
u=a//10000000
d=(a%10000000)//1000000
t=(a%1000000)//100000
c=(a%100000)//10000
q=(a%10000)//1000
s=(a%1000)//100
sep=(a%100)//10
oc=(a%10)//1

suma=oc*2+sep*3+s*4+q*5+c*6+t*7+d*2+u*3
print(suma)
digito=suma%11
final=11-digito
if final==11:
    dv=0
elif final==10:
    dv="k"
else:
    dv=final
print("dv=",dv)