#Cajero Automático
def Resultado(M,C=1000000,U=100000):
    if M > C:
        return "Monto no permitido"
    else:
        U = U - M
        C = C - M
        print("saldo cuenta=",U)
        print("saldo cajero=",C)
        return [U,C]
x = 0
y = 0
i = 0
while y == 0:
    if x == 0:
        print("Usuario")
        input()
        print("clave")
        c = input()
        if c == "1803":
            x = 1
        elif i == 2:
            print("Tarjeta bloqueada")
            break
        else:
            i += 1
    elif x == 1:
        print("Ingrese monto a retirar")
        re = input()
        f = "abcdefghijklmñopqrstuwvxyz,.-{}+´¿ABCDEFGHIJKLMÑOPQRSTUWVXYZ"
        if re in f:
            break
        elif re == "N":
            x = 1
        else:
            Resultado(float(re))
            