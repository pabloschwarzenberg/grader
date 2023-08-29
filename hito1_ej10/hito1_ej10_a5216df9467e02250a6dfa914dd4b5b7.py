#Cajero Automático
def usuario_confirmacion():
    while True:
        try:
            usuario= int(input("Ingrese usuario: "))
        except:
            print("Usuario invalido")
            break
        if usuario== 10334151:
            break                    
        else:
            print("Usuario invalido")
            break
    #for i in range(1):
    clave=int(input("Ingrese clave: "))
    if clave == 1803:
        return True
        #else:
            #print("clave invalida")
    print("Tarjeta bloqueada")
    return False

def cajero():
    while True:
        billetes20000=0
        billetes10000=0
        billetes5000=0
        contador_billetes=0
        cajero_plata=1000000
        confirmao=usuario_confirmacion()
        if confirmao==True:
            saldo=100000
            retiro= int(input("Cuanto retirara: "))
            if retiro <0 or retiro>1000000:
                print("Monto no permitido")
            else: 
                cajero_plata -= retiro
                saldo-=retiro
                saldo_cuenta= 'saldo cuenta=%s' %(str(saldo))
                saldo_cajero= 'saldo cajero=%s' %(str(cajero_plata))
                resultado= [saldo_cuenta,saldo_cajero] 
                while contador_billetes != retiro:   
                    if contador_billetes < retiro:
                        contador_billetes+=20000
                        billetes20000 += 1  
                    if contador_billetes > retiro:
                        contador_billetes-=20000
                        contador_billetes+=5000
                        billetes20000-=1
                        billetes5000+=1  
               
            

                return print(resultado)
        elif confirmao==False:
            print("Chao")
            break

cajero()

