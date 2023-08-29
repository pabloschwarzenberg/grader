#Cajero Automático
def retirar(num,platau,platac):
    if num > platau or num == 0:
        return False
    return True

usuario=10334151
clave=1803
platau=100000
platac=1000000
veces=0
c="no clave"

print("Bienveido al cajero automatico")
a=int(input("Ingrese usuario: "))
b=True
while b==True:
    if a!=usuario:
        print("Usuario invavildo")
        a= int(input("Ingrese usuario: "))
    if a == usuario:
        b=False
        if c!="clave":
            s=int(input("Ingrese clave: "))
        while s != clave and veces <= 1:
            veces=veces+1
            print("Clave invavilda")
            s=int(input("Ingrese clave: "))
            if veces > 1:
                print("Tarjeta bloqueada")
                break
        if s == clave:
            d=int(input("Ingrese monto a retirar(máx. es $"+str(platau)+"): "))
            x=retirar(d,platau,platac)
            while x==False:
                print("Monto invalido")
                d=int(input("Ingrese monto a retirar(máx. es $"+str(platau)+"): "))
                x=retirar(d,platau,platac)
            if x==True:
                print("Retiraste: $",d)
                platau=platau-d
                print("Saldo cuenta=",platau)
                platac=platac-d
                print("Saldo cajero=",platac)
            c="clave"
        r=input("Si desea realizar otra operación presione N, para terminar presione cualquier otra tecla: ")
        if r=="N":
            b=True
        else:
            b=False

            
      