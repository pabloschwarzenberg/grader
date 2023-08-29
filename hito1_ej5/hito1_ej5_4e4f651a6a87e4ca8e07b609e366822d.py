#Cálculo del dígito verificador de un rut
a= input("RUT :")
b= "32765432"
if (len(a)==8):
    c= int(a[0])*int(b[0])
    d= int(a[1])*int(b[1])
    e= int(a[2])*int(b[2])
    f= int(a[3])*int(b[3])
    g= int(a[4])*int(b[4])
    h= int(a[5])*int(b[5])
    i= int(a[6])*int(b[6])
    j= int(a[7])*int(b[7])
    k= c+d+e+f+g+h+i+j
    l= int(k)%11
    dv= 11-l
    
    if (dv==10):
        print("dv=k")
    else:
        print("dv=",dv)
        
    if (dv==11):
        print("dv=0")
    else:
        print("dv=",dv)
    
elif (len(a)==7):
    c= int(a[0])*int(b[1])
    d= int(a[1])*int(b[2])
    e= int(a[2])*int(b[3])
    f= int(a[3])*int(b[4])
    g= int(a[4])*int(b[5])
    h= int(a[5])*int(b[6])
    i= int(a[6])*int(b[7])
    k= c+d+e+f+g+h+i
    l= int(k)%11
    dv= 11-l
    if (dv==10):
        print("dv=k")
    else:
        print("dv=",dv)
    if (dv==11):
        print("dv=0")
    else:
        print("dv=",dv)