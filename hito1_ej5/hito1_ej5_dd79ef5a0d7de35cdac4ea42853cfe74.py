rut=int(input("Ingrese RUT: "))
if rut>=1000000 and rut<=9999999:
    a=rut//1000000
    b=rut//100000-a*10
    c=rut//10000-a*100-b*10
    d=rut//1000-a*1000-b*100-c*10
    e=rut//100-a*10000-b*1000-c*100-d*10
    f=rut//10-a*100000-b*10000-c*1000-d*100-e*10
    g=rut%10
    suma=g*2+f*3+e*4+d*5+c*6+b*7+a*2
    division=suma//11
    resto=suma-(11*division)
    dv=11-resto
else :
    a=rut//10000000
    b=rut//1000000-a*10
    c=rut//100000-a*100-b*10
    d=rut//10000-a*1000-b*100-c*10
    e=rut//1000-a*10000-b*1000-c*100-d*10
    f=rut//100-a*100000-b*10000-c*1000-d*100-e*10
    g=rut//10-a*1000000-b*100000-c*10000-d*1000-e*100-f*10
    h=rut%10
    suma=h*2+g*3+f*4+e*5+d*6+c*7+b*2+a*3
    division=suma//11
    resto=suma-(11*division)
    dv=11-resto

if dv==11: print("dv=0")
elif dv==10: print("dv=K")
else: print("dv= ",dv)





