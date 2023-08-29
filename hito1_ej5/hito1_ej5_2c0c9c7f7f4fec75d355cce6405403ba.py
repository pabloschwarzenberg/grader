#Cálculo del dígito verificador de un rut
rut=int(input())
d8=rut%10
d7=(rut%100)//10
d6=(rut%1000)//100
d5=(rut%10000)//1000
d4=(rut%100000)//10000
d3=(rut%1000000)//100000
d2=(rut%10000000)//1000000
d1=(rut%100000000)//10000000
total=((d8*2)+(d7*3)+(d6*4)+(d5*5)+(d4*6)+(d3*7)+(d2*2)+(d1*3))
mod=(11-(total%11))
if mod==11:
 dv=0
elif mod==10:
 dv="K"
else:
 dv=mod   
print("dv=",dv)