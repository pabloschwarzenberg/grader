#Cajero Automático
#Variables Iniciales
SCa  = 1000000
SC   = 100000
User = 10334151
Pass = 1803
VT   = 0
X    = 0
Y    = 0
Z    = 0
VK   = 20
DK   = 40
CK   = 40
#FuncionPrincipalBilletes
def contbill(monto):
    while monto != 0:
        if monto >= 20000:
            A  = monto//20000  # cantidad de billetes
            if A < VK:
                monto = monto - (A*20000) # Monto despues de quitarle la parte entera
                print("Billetes de 20000 = {0}" .format(A))
        else:
            print("Billetes de 20000 = 0")
        if monto >= 10000:
            B  = monto//10000
            if B < DK:
                monto = monto - (B*10000)
                print("Billetes de 10000 = {0}" .format(B))
        else:
            print("Billetes de 10000 = 0")
        if monto >= 5000:
            C  = monto//5000
            if C < CK:
                monto = monto - (C*5000)
                print("Billetes de 5000 = {0}" .format(C))
        else:
            print("Billetes de 5000 = 0")
#MainLoop
while VT == 0:
    IU = int(input("Ingrese el Usuario: "))
    while VT == 0:
        IC = int(input("Ingrese su Contraseña: "))
        if IC == Pass:
            #Bucle Para Montos
            while VT == 0:
                Y  = input("Ingrese el monto a retirar: ")
                #No entendi Bien la parte del break por las letras. Esta fue mi intepretacion.
                if Y in("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"):
                    VT = 1
                else:
                    Y  = int(Y)
                    Yx = Y
                    if Y < 5000:
                        pass
                    else:
                        if Y > SC:
                            print("Monto No Permitido")
                        else:
                            SCa   = SCa - Y
                            SC    = SC - Y
                            VKu   = 0
                            Dku   = 0
                            Cku   = 0
                            print("Saldo Cuenta = {0}" .format(SC))
                            print("Saldo Cajero = {0}" .format(SCa))
                            contbill(Yx)
                            if SC == 0:
                                VT = 1
        else:
            X = X + 1
            if X <= 2:
                print("Clave Invalida")
            if X == 3:
                print("Tarjeta Bloqueada")
                VT = 1
            #Fin Condicional; Fin De Programa