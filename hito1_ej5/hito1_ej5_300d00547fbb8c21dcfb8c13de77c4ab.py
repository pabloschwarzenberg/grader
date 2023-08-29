#Cálculo del dígito verificador de un rut
rut=list(input())
rut=rut[::-1]
print(rut)
multiplos=[2,3,4,5,6,7,2,3,4,5,6,7]
#27962409
print(multiplos[4])
cont=0
suma=0

for i in range(len(rut)):
    m=(int(rut[i]))*(multiplos[i])
    cont+=1
    suma=suma+m

x=int(suma/11)
x=x*11
y=suma-x
z=11-y

if 0<=z<10:
    print("dv=",z)

else:
    if z==11:
        print("dv=0")
        
    elif z==10:
        print("dv=k")
