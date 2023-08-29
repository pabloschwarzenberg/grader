#Cálculo del dígito verificador de un rut
rut=int(input("ingrese el rut sin digito verificador: "))
rte= str(rut)
len(rte)
if len(rte)==8:
    a=float(rte[0])
    b=float(rte[1])
    c=float(rte[2])
    d=float(rte[3])
    e=float(rte[4])
    f=float(rte[5])
    g=float(rte[6])
    h=float(rte[7])
    dv1=((a*3)+(b*2)+(c*7)+(d*6)+(e*5)+(f*4)+(g*3)+(h*2))
else:
    a=float(rte[0])
    b=float(rte[1])
    c=float(rte[2])
    d=float(rte[3])
    e=float(rte[4])
    f=float(rte[5])
    g=float(rte[6])
    dv1=((a*2)+(b*7)+(c*6)+(d*5)+(e*4)+(f*3)+(g*2))

dv2 = dv1 // 11

dv3 = dv1 - (11 * dv2)

dv4 = 11 - dv3

if dv4 == 11:
    print ("dv=0")
    
elif dv4 == 10:
    print ("dv=k")
    
else:
    print("dv=", dv4)
