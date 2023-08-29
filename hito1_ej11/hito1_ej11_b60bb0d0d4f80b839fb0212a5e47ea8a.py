print("Bienvenido a Banco PENTA")
U=input("Nº de usuario:")
contador=0
while contador<=2:
    C1=int(input("Ingrese su clave:"))
    if C1==1803:
        M=input("Monto a retirar:")
        MI=int(M)
        ms=str(M)
        if MI<=100000:
           
            
            a1=int(ms[0])
            a2=int(ms[1])
            mr=a1*10000+a2*1000
            print(mr)
            print("Monto permitido")
            print("Saldo cuenta=",100000-MI)
            print("Saldo cajero=",1000000-MI)
            
            if a1%2==0:
                print("billetes 20000=",int(a1/2))
                print("billetes  5000=",int(a2/5))
            if a1%2==1:
                
                print("billetes  10000=",a1)
                print("billetes  5000=",int(a2/5))
            if C1==1803:
                break
    else:
        print("clave incorrecta intente denuevo")
        contador+=1
    if contador==3:
        print("Tarjeta bloqueada")
        break
