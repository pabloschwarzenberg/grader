#Descomponer un número
a=(input())
j=int(a[:4])
    












if(j<10):
    c=a[0]
    print(c+"U")
elif(9<j<100):
    c=a[0]
    d=a[1]
    print(c+"D+"+d+"U")
elif(99<j<1000):
    c=a[0]
    d=a[1]
    e=a[2]
    
    print(c+"C+"+d+"D+"+e+"U")
elif(999<j<10000):
    c=a[0]
    d=a[1]
    e=a[2]
    f=a[3]
    print(c+"M+"+d+"C+"+e+"D+"+f+"U")