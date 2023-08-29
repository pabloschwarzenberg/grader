#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese su rut:"))
if rut<=9999999:
        
        a=rut//10**6
        b=(rut-(10**6*a))//10**5
        c=(rut-(10**6*a)-(10**5*b))//10**4
        d=(rut-(10**6*a)-(10**5*b)-(10**4*c))//10**3
        e=(rut-(10**6*a)-(10**5*b)-(10**4*c)-(10**3*d))//10**2
        f=(rut-(10**6*a)-(10**5*b)-(10**4*c)-(10**3*d)-(10**2*e))//10**1
        g=(rut-(10**6*a)-(10**5*b)-(10**4*c)-(10**3*d)-(10**2*e)-(10**1*f))//1


        h=g*2
        i=f*3
        j=e*4
        k=d*5
        l=c*6
        m=b*7
        n=a*2


        suma=h+i+j+k+l+m+n
        div=suma//11
        resto=suma-div*11
        digito=11-resto

        if digito==10:
                print("dv=k")
        if digito==11:
                print("dv=0")

        elif digito!=11!=10:
                print("dv=",digito)

elif rut>9999999:

        
        A=rut//10**7
        B=(rut-(10**7*A))//10**6
        C=(rut-(10**7*A)-(10**6*B))//10**5
        D=(rut-(10**7*A)-(10**6*B)-(10**5*C))//10**4
        E=(rut-(10**7*A)-(10**6*B)-(10**5*C)-(10**4*D))//10**3
        F=(rut-(10**7*A)-(10**6*B)-(10**5*C)-(10**4*D)-(10**3*E))//10**2
        G=(rut-(10**7*A)-(10**6*B)-(10**5*C)-(10**4*D)-(10**3*E)-(10**2*F))//10
        H=(rut-(10**7*A)-(10**6*B)-(10**5*C)-(10**4*D)-(10**3*E)-(10**2*F)-(10**1*G))//1
           
           
        suma2=(H*2)+(G*3)+(F*4)+(E*5)+(D*6)+(C*7)+(B*2)+(A*3)
        div2=suma2//11 
        resto2=suma2-div2*11
        (digito2)=11-resto2

        if (digito2)!=11 and (digito2)!=10:
           print("dv=",(digito2))

        elif (digito2)==10:
           print("dv=k")
        elif (digito2)==11:
           print("dv=0")
