RUT=input("RUT:")
RUTA=str(RUT)
RUTB=int(RUT)
# 19689182
if RUTB>9999999:
    a1=int(RUTA[0])
    a2=int(RUTA[1])
    a3=int(RUTA[2])
    a4=int(RUTA[3])
    a5=int(RUTA[4])
    a6=int(RUTA[5])
    a7=int(RUTA[6])
    a8=int(RUTA[7])
    b=a1*3
    c=a2*2
    d=a3*7
    e=a4*6
    f=a5*5
    g=a6*4
    h=a7*3
    i=a8*2
    S=b+c+d+e+f+g+h+i
    R=(S%11)
    
    CF=11-R
    

else:
    a1=int(RUTA[0])
    a2=int(RUTA[1])
    a3=int(RUTA[2])
    a4=int(RUTA[3])
    a5=int(RUTA[4])
    a6=int(RUTA[5])
    a7=int(RUTA[6])
    b=a1*2
    c=a2*7
    d=a3*6
    e=a4*5
    f=a5*4
    g=a6*3
    h=a7*2
    S=b+c+d+e+f+g+h
    R=(S%11)
    
    CF=11-R
    CF=int(CF)
    print("resto:",R)
if CF==10:
    CF="K"
    
if R==0:
    CF=0

print("dv=",CF)