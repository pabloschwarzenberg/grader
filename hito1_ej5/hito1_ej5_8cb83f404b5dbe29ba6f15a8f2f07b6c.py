#Cálculo del dígito verificador de un rut      
rut=int(input("Ingrese RUT aquí:"))
q=(rut//10000000)*3
w=((rut//1000000)%10)*2 
e=((rut//100000)%10)*7
r=((rut//10000)%10)*6
t=((rut//1000)%10)*5
y=((rut//100)%10)*4
u=((rut//10)%10)*3
i=((rut//1)%10)*2
suma=(q+w+e+r+t+y+u+i)
resto=suma//11
result=suma-(11*resto)
resta=11-result
if resta == 11:
    print("dv=",end="")
    print("0")
elif resta == 10:
    print("dv=",end="")
    print("k")
else:
    print("dv=",end="")
    print(resta)