#Cajero Automático
s_c = 1000000 
s_u = 100000 

b_d_20 = 20000
b_d_10 = 10000
b_d_5 = 5000

N = True
while(N):
    cd20 = 0
    cd10 = 0
    cd5 = 0
    try:
       u = input("ingrese usuario: ")
    except EOFError:
       break
    try:
       c = input("ingrese clave: ")
    except EOFError:
       break
    try:
        m = int(input("ingrese monto"))
    except ValueError:
        break
  
    while (len(u) != 8):
    
            print("usuario no encontrado")
            u = input("ingrese usuario")

            if(len(u) == 8):
                break
                      
    e = 1   
    while(e < 3):
                
          if(len(c) == 4):
              break
    
          if(len(c) != 4):
                 e = e + 1
                 print("Clave invalida")                 
                 c = input("ingrese contraseña")                 
                        
          if(e == 3):
                  print("tarjeta bloqueada")
                  break
    
    if(s_c - m > 0):
        s_c= s_c - m
        
    else:
        print("No hay Suficiente dinero en este cajero")
        
    if(s_u - m>0):
        s_u= s_u - m
    else:
        print("Sobregiro")
    
    while(m//20000):
        cd20 += 1
        m = m - 20000
        
    while(m//10000):
        cd10 += 1
        m = m - 10000
    
    while(m//5000):
        cd5 += 1
        m = m - 5000

    print("billetes 20000=",cd20)
    print("billetes 10000=",cd10)
    print("billetes 5000=",cd5)
    print("saldo cuenta=",s_u)
    print("saldo cajero=",s_c)
    
    s = input("Ingrese N para salir: ")
    
    if(s == "N"):
        N = False