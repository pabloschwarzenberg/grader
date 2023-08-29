#Cajero Automático
def giro(m):
    b5=40
    b10=40
    b20=20
    s=b5*5000+b10*10000+b20*20000
    m2=m/1000
    print((m2/5)%2)
    m3=round((m/10000),0)
    print(m3)
    m4=round((m3/2),0)
    b5n=0
    b10n=0
    b20n=0
    if (m2/5)%2!=0:
        b5n+=1
    if (m3%2)!=0:
        b10n+=1
        m4-=1
    b20n+=m4
    b20-=m4
    s2=b5n*5000+b10n*10000+b20n*20000
    return (s2,b5n,b10n,b20n)
    

usuario = int(input("Ingrese el usuario: "))
clave = int(input("Ingrese su clave: "))

intentos = 1
saldo_cajero = 1000000
saldo_usuario = 100000
user = 10334151
passw = 1803

while clave != passw:
    intentos += 1
    
    if clave == passw:
        print("clave incorrecta")
        break

    if intentos > 3:
        break

    clave = int(input("Ingrese de nuevo su clave: "))


if intentos > 3:
    print("tarjeta bloqueada")

if usuario == user:
    
    if clave == passw:
        
        monto = int(input("¿Cuanto quiere retirar?: "))
    
        if monto > saldo_usuario and monto > saldo_cajero:
            
            print("monto no perimitido")

        else:
            saldo_usuario -= monto
            saldo_cajero  -= monto
            b5d=int(giro(monto)[1])
            b10d=int(giro(monto)[2])
            b20d=int(giro(monto)[3])
            sn=int(round((giro(monto)[0]),0))
            print("saldo cuenta="+str(saldo_usuario))
            print("saldo cajero="+str(saldo_cajero))
            print("giro: ",sn)
            print("\nbilletes de 20000: ",b20d)
            print("\nbilletes de 10000: ",b10d)
            print("\nbilletes de 5000: ",b5d)

