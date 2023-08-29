E = float(input("ingrese un numero entero de 4 cifras"))
if E <9999:
    U  = E / 1000
    UEntero = int(U)
    D  = (E - (UEntero*1000)) / 100
    DEntero = int(D)
    C  = (E - ((UEntero*1000)+(DEntero*100))) / 10
    CEntero = int(C)
    UM = (E - ((UEntero*1000)+(DEntero*100)+(CEntero*10))) / 1
    UMEntero = int(UM)
    print(f"{UMEntero}M + {CEntero}C + {DEntero}D + {UEntero}U")

   