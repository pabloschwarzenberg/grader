#Cajero Automático
veinte=20
diez=40
cinco=40
cajero=veinte*20000+diez*10000+cinco*5000
n=0
usuario=int(input("Bienvenido, ingrese su rut sin digito verificador: "))
cuenta=100000
clave=int(input("Ingrese su clave: "))
while clave!=1803 and n<3:
    print("clave invalida")
    n=n+1
    clave=int(input("Ingrese su clave: "))
if n==3:
    print("tarjeta bloqueada")
else:
    monto=int(input("Ingrese el saldo a retirar: "))
    if monto>cajero or monto%5000!=0:
        print("monto no permitido")
    else:
        print("billetes 20000=",(monto//20000))
        print("billetes 10000=",((monto%20000)//10000))
        print("billetes 5000=",(((monto%20000)%10000)//5000))
        print("saldo cuenta=",cuenta-monto)
        print("saldo cajero=",cajero-monto)
        veinte=veinte-(monto//20000)
        diez=diez-((monto%20000)//10000)
        cinco=cinco-(((monto%20000)%10000)//5000)      