def ingresar(usuario):    
    x=0
    while x<3:
        clave=input("Ingrese clave: ")
        if clave == "1803":
            x+=3
            return True
        if clave != "1803":
            x+=1
            print("clave invalida")
    if x==3:
        print("tarjeta bloqueada")
        return False
    
def retirar(ingreso,cajero,cuenta):
    if  ingreso==True:
        x="SEGUIR"
        while x=="SEGUIR":
            monto=input("Ingrese monto a retirar: ")
            if monto.isdigit():
                if  int(monto)>cajero or int(monto)>cuenta:
                    print("monto no permitido")
                    x="NoSeguir"
                else:
                    cajero-=int(monto)
                    cuenta-=int(monto)
                if cuenta>0:
                    x="SEGUIR"
                else:
                    x="NoSeguir"
                print("saldo cuenta="+str(cuenta))
                print("saldo cajero="+str(cajero))
            else:
                if monto != "N":
                    x="NoSeguir"
cajero=1000000
cuenta=100000 
ingreso=ingresar(input("Ingrese usuario: "))
retirar(ingreso,cajero,cuenta)