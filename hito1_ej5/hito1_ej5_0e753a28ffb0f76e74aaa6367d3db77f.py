#Cálculo del dígito verificador de un rut
rut=int(input("ingrese su rut\n"))
a=rut//10000000
b=(rut-a*10000000)//1000000
c=(rut-a*10000000-b*1000000)//100000
d=(rut-a*10000000-b*1000000-c*100000)//10000
e=(rut-a*10000000-b*1000000-c*100000-d*10000)//1000
f=(rut-a*10000000-b*1000000-c*100000-d*10000-e*1000)//100
g=(rut-a*10000000-b*1000000-c*100000-d*10000-e*1000-f*100)//10
h=(rut-a*10000000-b*1000000-c*100000-d*10000-e*1000-f*100)%10
#multiplicación:
valor=(h*2)+(g*3)+(f*4)+(e*5)+(d*6)+(c*7)+(b*2)+(a*3)
valor2=valor//11
valor3=valor-(valor2*11)
dv=11-valor3
if dv==11:
    print ("dv=",0)
elif dv==10:
    print ("dv=","k")
else:
    print("dv=",dv)