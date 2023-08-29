#Sistema de Ecuaciones
arr=[]

for i in range(6):
    coef=eval(input("ingrese el coeficiente: "))
    arr.append(coef)
a,b,c,d,e,f=arr[0],arr[1],arr[2],arr[3],arr[4],arr[5]
y=((f*a)-(d*c))/((e*a)-(d*b))
x=(c-(b*y))/a
print("x=",x)
print("y=",y)

 