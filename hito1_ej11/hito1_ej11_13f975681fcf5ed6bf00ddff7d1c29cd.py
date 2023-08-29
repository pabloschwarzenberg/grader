cuenta=int(input("ingresar cuenta"))
saldobanco=1000000
Billetes20=20
Billetes10=40
Billetes5=40
conteo=0
while(cuenta!=10334151):
    cuenta=int(input("ingresar cuenta"))
if(cuenta==10334151):
    clave=int(input("ingresar clave"))
    if(clave==1803):
        saldo=100000
        m=int(input("monto a retirar"))
        if(m<=100000):
            saldo=saldo-m
            saldobanco=saldobanco-m
            A=m//100000
            B=m-A*100000
            C=B//10000
            D=B-C*10000
            E=D//5000
            print("saldo cuenta=",saldo,"saldo cajero=",saldobanco)
            print("billetes 20000=",A)
            print("billetes 10000=",C)
            print("billetes 5000=",E)
            if(m>1000000):
                print("monto no permitido")
    while(clave!=1803)and (conteo<3):
            conteo=conteo+1
            print("clave invalida")
            clave=int(input("ingresar clave"))
    if(conteo==3):
                print("tarjeta bloqueada")
                str(input("ingresar letra distinta de N para salir"))