#Cálculo del dígito verificador de un rut
 #Digito Verificador RUT
#Input de rut

n = int(input("Ingrese su rut:  "))

if 999999 < n < 100000000:
    R8= n%10
    n = n//10
    R7 = n%10
    n = n//10
    R6 = n%10
    n = n//10
    R5 = n%10
    n = n//10
    R4 = n%10
    n = n//10
    R3 = n%10
    n = n//10
    R2 = n%10
    n = n//10
    R1 = n

    RR8 = R8*2
    RR7 = R7*3
    RR6 = R6*4
    RR5 = R5*5
    RR4 = R4*6
    RR3 = R3*7
    RR2 = R2*2
    RR1 = R1*3
    
    SUMA = (RR8+RR7+RR6+RR5+RR4+RR3+RR2+RR1)

    RESTO = SUMA % 11

    if 2 <= RESTO <= 10:
        DV = 11 - RESTO
        print("dv=",DV)
    elif RESTO == 1:
        print("dv=k")
    elif RESTO == 0:
        print("dv=0")
        
    else:
        print("dv=0")        
        

elif 99999 < n < 10000000:
    R7 = n%10
    n = n//10
    R6 = n%10
    n = n//10
    R5 = n%10
    n = n//10
    R4 = n%10
    n = n//10
    R3 = n%10
    n = n//10
    R2 = n%10
    n = n//10
    R1 = n

    RR7 = R7*3
    RR6 = R6*4
    RR5 = R5*5
    RR4 = R4*6
    RR3 = R3*7
    RR2 = R2*2
    RR1 = R1*3
    
    SUMA = (RR7+RR6+RR5+RR4+RR3+RR2+RR1)

    RESTO = SUMA % 11

    DV = 11 - RESTO
    
    if 2 <= RESTO <= 10:
        DV = 11 - RESTO
        print("dv=",DV)
    elif RESTO == 1:
        print("dv=k")
    elif RESTO == 0:
        print("dv=0")
        
else:
    print("Numero Invalido")