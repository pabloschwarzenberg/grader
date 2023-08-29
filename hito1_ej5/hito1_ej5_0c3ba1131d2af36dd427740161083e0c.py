#Cálculo del dígito verificador de un rut
a=int(input())

if(10000000<=a<100000000):
    a=str(a)
    b=3*int(a[0])+int(a[1])*2+int(a[2])*7+int(a[3])*6+int(a[4])*5+int(a[5])*4+int(a[6])*3+int(a[7])*2
    c=b%11
    d=11-c
    
    if(d==10):
        print("dv=k")
    if(c==0) and (d!=10):
        print("dv=0")
    else:
        d=str(d)
        print("dv="+d)
        
    
    
   

else:
    a=str(a)
    b1=2*int(a[0])+int(a[1])*7+int(a[2])*6+int(a[3])*5+int(a[4])*4+int(a[5])*3+int(a[6])*2
    
    c1=b1%11
    
    
    d1=11-c1
    
    
    if(d1==10):
        
        print("dv=k")
    if(c1==0) and (d1!=10):
        print("dv=0")
    else:
        
        d1=str(d1)
        print("dv="+d1)