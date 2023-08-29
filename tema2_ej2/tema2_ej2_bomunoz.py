def amigos(a,b):
    suma_1=0
    h=0
    j=0
    for i in range(1,a):
        if a%i==0:
            suma_1=suma_1+i
    suma_2=0
        
    for i in range (1,b):
        if (b%i==0):
          suma_2=suma_2+i
    if a==suma_1 and b==suma_1:
        h=b
    else:
        j=b
    return b==suma_1
               