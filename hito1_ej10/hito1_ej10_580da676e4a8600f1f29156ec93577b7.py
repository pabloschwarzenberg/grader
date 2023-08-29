#Cajero Automático
s_c = 1000000 
s_u = 100000 

N = True
while(N):
    try:
       u = input("ingrese usuario: ")
    except EOFError:
       break
    
    
    while (len(u) != 8):
    
            print("usuario no encontrado")
            u=input("ingrese usuario: ")
            if(len(u) == 8):
                break
    
    c = input("ingrese contraseña: ")

    e = 1   
    while(e < 3):
                
          if(len(c) == 4):
              break
    
          if(len(c) != 4):
                 e = e + 1
                 print("Clave invalida")
                 
                 c = input("ingrese contraseña: ")
                                                         
          if(e == 3):
                  print("targeta bloqueada")
                  break

    m = int(input("ingrese monto: "))    
    while((m > 100000) or (m < 0)):
        print("monto no permitido")
        
        m = int(input("ingrese monto: "))       
        if((m <= 100000) or (m >= 0)):
            break
            
    s_c_r=s_c - m
    s_u_r = s_u - m

    print("saldo cuenta = ",s_u_r)
    print("saldo cajero = ",s_c_r)
    
    s = input("Ingrese N para salir: ")
    
    if(s=="N"):
        N=False