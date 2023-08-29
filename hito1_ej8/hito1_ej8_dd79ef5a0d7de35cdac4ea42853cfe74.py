numero=int(input("Ingrese numero: "))
if not numero<1000 and numero>9999:
    print("Error")
else:
    M=numero//1000
    C=numero//100-M*10
    D=numero//10-M*100-C*10
    U=numero%10
    numerocaracter=str(numero)
    if len(numerocaracter)==4:
        print(M,"M + ",C,"C + ",D,"D + ",U,"U")
    if len(numerocaracter)==3:
        print(C,"C + ",D,"D + ",U,"U")
    if len(numerocaracter)==2:
        print(D,"D + ",U,"U")
    if len(numerocaracter)==1:
        print(U,"U")
    
    
    
    
        
                
                       



