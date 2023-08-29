#.Cajero automático
def ingreso_sesion(usuario,clave):
    if usuario==10334151:
        cuenta=0
        while clave!=1803:
            clave=int(input("clave invalida: "))
            cuenta=cuenta+1
            if cuenta==3:
                print("Tarjeta bloqueada")
                break
def retiro_dinero(dinero):
    cuenta=0
    deseacontinuar=''
    saldo_inicial=1000000
    dinero_cta=100000
    while deseacontinuar!='N' or deseacontinuar!='n':
        if cuenta>=1:
            dinero=int(input("Ingrese monto a retirar: "))
        while dinero>dinero_cta:
            print("Monto no permitido")
            dinero=int(input("Ingrese monto a retirar: "))
        saldo_cta=dinero_cta-dinero
        saldo_cajero=saldo_inicial-dinero
        saldo_inicial=saldo_cajero #.nuevo saldo cajero
        dinero_cta=saldo_cta #.nuevo saldo cuenta cliente
        cuenta=cuenta+1
        print("saldo cuenta="+str(saldo_cta))
        print("saldo cajero="+str(saldo_cajero))
        deseacontinuar=input()
        if deseacontinuar=='N' or deseacontinuar=='n':
            break
        
if __name__ == "__main__":
    usuario=int(input("Ingrese usuario: "))
    clave=int(input("Ingrese clave: "))
    dinero=int(input("Ingrese monto a retirar: "))
    ingreso=ingreso_sesion(usuario,clave)
    retiro=retiro_dinero(dinero)

