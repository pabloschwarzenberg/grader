#Cálculo del dígito verificador de un rut
rut=input("RUT:")
rutc=str(rut)
rutn=int(rut)
if 9999999<rutn:
    rutc.split(" ")
    
    d8=int(rutc[7])
    d7=int(rutc[6])
    d6=int(rutc[5])
    d5=int(rutc[4])
    d4=int(rutc[3])
    d3=int(rutc[2])
    d2=int(rutc[1])
    d1=int(rutc[0])

    #print("d8:",d8)
    #print(d7)
    #print(d6)
    #print(d5)
    #print(d4)
    #print(d3)
    #print(d2)
    #print("d1:",d1)
    
    
    d8=2*d8
    d7=3*d7
    d6=4*d6
    d5=5*d5
    d4=6*d4
    d3=7*d3
    d2=2*d2
    d1=3*d1
    suma=d1+d2+d3+d4+d5+d6+d7+d8
    #print(suma)
    div=suma%11
    dv=11-div
    if dv==10:
        dv="k"
    if div==0:
        dv=0
    print("dv=",dv)
else:
    rutc.split(" ")
    
    
    d7=int(rutc[6])
    d6=int(rutc[5])
    d5=int(rutc[4])
    d4=int(rutc[3])
    d3=int(rutc[2])
    d2=int(rutc[1])
    d1=int(rutc[0])

   
    print(d7)
    print(d6)
    print(d5)
    print(d4)
    print(d3)
    print(d2)
    print("d1:",d1)

    
    d7=2*d7
    d6=3*d6
    d5=4*d5
    d4=5*d4
    d3=6*d3
    d2=7*d2
    d1=2*d1

    print(d7)
    print(d6)
    print(d5)
    print(d4)
    print(d3)
    print(d2)
    print("d1:",d1)

    suma=d1+d2+d3+d4+d5+d6+d7
    print(suma)
    div=suma%11

    dv=11-div
    if dv==10:
        dv="k"
    if div==0:
        dv=0
    print("dv=",dv)
       