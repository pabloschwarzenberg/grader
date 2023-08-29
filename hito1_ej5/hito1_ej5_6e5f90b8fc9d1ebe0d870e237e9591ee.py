#Cálculo del dígito verificador de un rut
rut= (input())  
    
        








if(len(rut)<=7):
    a = int(rut[0])*9
    b = int(rut[1])*4
    c = int(rut[2])*5
    d = int(rut[3])*6
    e = int(rut[4])*7
    f = int(rut[5])*8
    g = int(rut[6])*9
    

    
    
      
    suma7= a+b+c+d+f+g+e
    resto = int(suma7)%11
    dv = resto 
    if(dv==10):
       print("dv = k")
    else:
                       print('dv =',dv)

else:
    if(len(rut)==8):
        l = int(rut[0])*8
        m = int(rut[1])*9
        n = int(rut[2])*4
        o = int(rut[3])*5
        p = int(rut[4])*6
        q = int(rut[5])*7
        r = int(rut[6])*8
        s= int(rut[7])*9

        suma8= l+m+n+o+p+q+r+s
        rest= int(suma8)%11
        if(rest==10):
            print("dv = k")
        else:
            print('dv =',rest)