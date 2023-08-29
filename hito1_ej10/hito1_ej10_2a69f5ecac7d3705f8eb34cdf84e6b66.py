usuario=""
clave=""
op=3
while op>0 and (usuario!="10334151" or clave!="1803"):
    usuario=input("usuario: ")
    clave= input("clave: ")
    if usuario!="10334151" and clave!="1803":
        print("clave invalida")
        op-=1
    if op==0:
        print("tarjeta bloqueada")
        
if usuario=="10334151" and clave=="1803":
    seguir="N"
    saldo_cajero=1000000
    saldo_cuenta=100000
    while seguir =="N":
        dinero=int(input("monto a retirar: "))

        if dinero>saldo_cuenta or dinero>saldo_cajero or dinero<0:
            print("monto no permitido")
        else:
            saldo_cajero-=dinero
            saldo_cuenta-=dinero
            print("saldo cuenta="+str(saldo_cuenta))
            print("saldo cajero="+str(saldo_cajero))
        seguir= input("continuar N: ")
      