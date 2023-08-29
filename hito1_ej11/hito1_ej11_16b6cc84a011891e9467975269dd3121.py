#Cajero Automático
cajero = 1000000
saldo = 100000
i = 0  

while i <= 3:
    usuario = eval(input("Ingresar usuario: ")) 
    clave = eval(input("Ingresar clave: "))    
    i = i + 1
    if usuario == 10334151 and clave == 1803:
        monto = eval(input("Ingresar monto de retiro: "))

        if monto <= saldo:
            cajero = cajero - monto
            saldo = saldo - monto
            print("saldo cuenta=",saldo)
            print("saldo cajero=",cajero)
            break
        else:
            print("monto no permitido")
    else:
        print("clave invalida")
    if i == 3:
        print("tarjeta bloqueada")
           
def nbEntregados(monto):
    
    nb20000 = 0
    nb10000 = 0
    nb5000 = 0
    
    while monto>0:
        if monto >= 20000:
            
            nb20000 = nb20000 + 1
            monto = monto - 20000
            
        elif monto >= 10000:
            
            nb10000 = nb10000 + 1
            monto = monto - 10000
            
        elif monto >= 5000:
            
            nb5000 = nb5000 + 1
            monto = monto - 5000
            
    return [nb20000, nb10000, nb5000]

L = nbEntregados(monto)

print("billetes 20000=" + str(L[0]))
print("billetes 10000=" + str(L[1]))
print("billetes 5000=" + str(L[2]))
      