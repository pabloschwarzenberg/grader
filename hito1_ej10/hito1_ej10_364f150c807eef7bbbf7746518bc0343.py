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
                    if Y > SC:
                        print("Monto No Permitido")
                    else:
                        SCa = SCa - Y
                        SC  = SC - Y
                        print("Saldo Cuenta = {0}" .format(SC))
                        print("Saldo Cajero = {0}" .format(SCa))
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