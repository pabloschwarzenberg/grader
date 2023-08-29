ID=10334151
CODE=1803
SCaj=1000000
s=100000
while True :
    NUS=(input("Ingrese numero de usuario: "))
    KEY=(input("Ingrese Clave: "))
    Nint=0
    if ID==NUS :
        while (Nint<3):
            if CODE==KEY :
                Mont=int(input("Ingrese monto a retirar:"))
                while Mont>s :
                    print("Monto no permitido")
                    Mont = int(input("Ingrese nuevo monto a retirar:"))
                if Mont<=s:
                    print("saldo cuenta",(s-Mont))
                    print("saldo cajero",(SCaj-Mont))
                    a=str(input("ingrese una letra: "))
                    print(a)
                    if (a != "N" or "n"):
                        break
            elif (KEY!=CODE and KEY!=0):
                Nint=Nint+1
                KEY=int(input("Clave invalida: ",))

                if (Nint==2):
                    print("tarjeta bloqueada")
                    break
