#Cajero Automático
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

#BLOQUE PRINCIPAL:
monto = 35000
L = nbEntregados(monto)

print("billetes 20000=" + str(L[0]))
print("billetes 10000=" + str(L[1]))
print("billetes 5000=" + str(L[2]))