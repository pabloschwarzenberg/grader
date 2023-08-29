#Ordenar tres números
v1=int(input("Ingrese el primer numero entero: "))
v2=int(input("Ingrese el segundo numero entero: "))
v3=int(input("Ingrese el tercer numero entero: "))
if v1<=v2<=3:
    print(v1,",",v2,",",v3)
elif v1<=v3<=v2:
    print(v1,",",v3,",",v2)
elif v2<=v1<=v3:
    print(v2,",",v1,",",v3) 
elif v2<=v3<=v1:
    print(v2,",",v3,",",v1)
elif v3<=v1<=v2:
    print(v3,",",v1,",",v2)
elif v3<=v2<=v1:
    print(v3,",",v2,",",v1)



