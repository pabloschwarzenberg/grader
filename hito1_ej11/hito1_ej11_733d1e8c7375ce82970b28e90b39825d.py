#funcion para revisar clave
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
    
#calcular cantidad de billetes, reemplazar numero de billetes
def cantidadBilletes(MONTO,b20,b10,b5):
    if str(MONTO).isdigit():
        if  MONTO//20000>=1 and b20>=MONTO//20000:
            billetesDe20=MONTO//20000
            MONTO-=20000*billetesDe20
            b20-=billetesDe20
            print("billetes 20000="+str(billetesDe20))
        if MONTO//10000>=1 and b10>=MONTO//10000:
            billetesDe10=MONTO//10000
            MONTO-=10000*billetesDe10
            b10-=billetesDe10
            print("billetes 10000="+str(billetesDe10))
        if MONTO//5000>=1 and b5>=(MONTO//5000):
            billetesDe5=MONTO//5000
            MONTO-=5000*billetesDe5
            b5-=billetesDe5
            print("billetes 5000="+str(billetesDe5))
    else:
        return False

    return(b20,b10,b5)
        
    
#funcion para hacer retiro    
def retirar(ingreso,cajero,cuenta,b20,b10,b5):
    if  ingreso==True:
        x="SEGUIR"
        while x=="SEGUIR":
            monto=input("Ingrese monto a retirar: ")
            if monto.isdigit():
                MONTO=int(monto)
            else:
                MONTO=monto
            if monto.isdigit():
                if  int(monto)>cajero or int(monto)>cuenta:
                    print("monto no permitido")
                    x="NoSeguir"
                else:
                    cajero-=int(monto)
                    cuenta-=int(monto)
                    print("saldo cuenta="+str(cuenta))
                    print("saldo cajero="+str(cajero))
                    z=cantidadBilletes(MONTO,b20,b10,b5)
                    if  z==False:
                        no="pasanasa"
                    else:
                        b20=z[0]
                        b10=z[1]
                        b5=z[2]
                if cuenta>0:
                    x="SEGUIR"
                else:
                    x="NoSeguir"
                    print(b20,b10,b5)
                
            else:
                if monto != "N":
                    x="NoSeguir"

#saldo inicial
cajero=1000000
cuenta=100000
#billetes
b_20000=20
b_10000=40
b_5000=40
#programa
ingreso=ingresar(input("Ingrese usuario: "))
retirar(ingreso,cajero,cuenta,b_20000,b_10000,b_5000)