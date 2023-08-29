saldo_cajero=1000000 
saldo_usuario=100000 

N=True
while(N):
    try:
       usuario=input("ingrese usuario: ")
    except EOFError:
       break
    
    
    while (len(usuario)!=8):
    
            print("usuario no encontrado")
            usuario=input("ingrese usuario: ")
            if(len(usuario)==8):
                break
    
    clave=input("ingrese contraseña: ")

    error=1   
    while(error<3):
                
          if(len(clave)==4):
              break
    
          if(len(clave)!=4):
                 error=error+1
                 print("Clave invalida")
                 
                 clave=input("ingrese contraseña: ")
                                                         
          if(error==3):
                  print("targeta bloqueada")
                  break

    monto=int(input("ingrese monto: "))    
    while((monto>100000)or(monto<0)):
        print("monto no permitido")
        
        monto=int(input("ingrese monto: "))       
        if((monto<=100000) or (monto>=0)):
            break
            
    saldo_cajero_resto=saldo_cajero-monto
    saldo_usuario_resto=saldo_usuario-monto

    print("saldo cuenta= ",saldo_usuario_resto)
    print("saldo cajero= ",saldo_cajero_resto)
    
    salida=input("Ingrese N para salir: ")
    
    if(salida=="N"):
        N=False