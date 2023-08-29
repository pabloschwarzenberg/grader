saldo_cajero=1000000 
saldo_usuario=100000 

billetes_de_20=20000
billetes_de_10=10000
billetes_de_5=5000

N=True
while(N):
    contadorde20=0
    contadorde10=0
    contadorde5=0
    try:
       usuario=input("ingrese usuario: ")
    except EOFError:
       break
    try:
       clave=input("ingrese clave: ")
    except EOFError:
       break
    try:
        monto=int(input("ingrese monto"))
    except ValueError:
        break
  
    while (len(usuario)!=8):
    
            print("usuario no encontrado")
            usuario=input("ingrese usuario")

            if(len(usuario)==8):
                break
                      
    error=1   
    while(error<3):
                
          if(len(clave)==4):
              break
    
          if(len(clave)!=4):
                 error=error+1
                 print("Clave invalida")                 
                 clave=input("ingrese contraseña")                 
                        
          if(error==3):
                  print("targeta bloqueada")
                  break
    
    if(saldo_cajero - monto>0):
        saldo_cajero= saldo_cajero - monto
        
    else:
        print("No hay Suficiente dinero en este cajero")
        
    if(saldo_usuario - monto>0):
        saldo_usuario= saldo_usuario - monto
    else:
        print("Sobregiro")
    
    while(monto//20000):
        contadorde20+=1
        monto=monto-20000
        
    while(monto//10000):
        contadorde10+=1
        monto=monto-10000
    
    while(monto//5000):
        contadorde5+=1
        monto=monto-5000

    print("billetes 20000=",contadorde20)
    print("billetes 10000=",contadorde10)
    print("billetes 5000=",contadorde5)
    print("saldo cuenta=",saldo_usuario)
    print("saldo cajero=",saldo_cajero)
    
    
    
    salida=input("Ingrese N para salir: ")
    
    if(salida=="N"):
        N=False