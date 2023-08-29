#Cálculo del dígito verificador de un rut
rut=int(input("ingresa rut:"))

if (rut/10000000)>1:
    a=rut%10
    b=rut%100//10
    c=rut%1000//100
    d=rut%10000//1000
    e=rut%100000//10000
    f=rut%1000000//100000
    g=rut%10000000//1000000
    h=rut//10000000
    suma=(a*2)+(b*3)+(c*4)+(d*5)+(e*6)+(f*7)+(g*2)+(h*3)
    resto=suma%11
    dv=11-resto
    if dv==10:
       dv="k"
    print("dv=",dv)
else:
    a=rut%10
    b=rut%100//10
    c=rut%1000//100
    d=rut%10000//1000
    e=rut%100000//10000
    f=rut%1000000//100000
    g=rut%10000000//1000000
    suma=(a*2)+(b*3)+(c*4)+(d*5)+(e*6)+(f*7)+(g*2)
    resto=suma%11
    dv=11-resto
    if dv==10:
       dv="k"
    
    if dv==11:
        dv="0"
    print("dv=",dv)



