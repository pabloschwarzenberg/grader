#Descomponer un número
n=int(input(" Ingrese un numero de hasta 4 digitos: "))
if n<10:
    print(n,"U")
    
elif n<100:
    D=int(n/10)
    U=int(n-(10*D))
    print(D,"D + ",U,"U")
    
elif n<1000:
    C=int(n/100)
    D=int((n-(100*C))/10)
    U=int(n-(100*C)-(D*10))
    print(C,"C + ",D,"D + ",U,"U")
    
else: 
    M=int(n/1000)
    C=int((n-(M*1000))/100)
    D=int((n-(M*1000)-(C*100))/10)
    U=int(n-(M*1000)-(C*100)-(D*10))
    print(M,"M + ",C,"C + ",D,"D + ",U,"U")    