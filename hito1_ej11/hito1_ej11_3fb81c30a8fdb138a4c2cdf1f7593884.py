#cajero automatico nivel 2
caj = 1000000
cantidad_billetes_20 = 20
cantidad_billetes_10 = 40
cantidad_billetes_5 = 40
billete_5 = 5000
cu = 100000
adm = "10334151"
c = "1803"
usuario = input("usuario: ")
if usuario == adm:
    contador = 0
    while contador < 3 :
        cla = input("clave: ")
        if cla != c :
            cont += 1
            print("clave invalida")
            continue
        ret = eval(input("cuanto dinero desea retirar: "))
        if ret > 100000:
            print("monto no permitido")
        else:
            #cuenta de billetes
            suma = 1
            while True:
                if billete_5 * suma == ret :
                    break
                suma += 1
            print(suma)
            saldo_cajero = caj - ret
            saldo_cuenta = cu - ret
            print("saldo cuenta=", saldo_cuenta, "\nsaldo cajero=", saldo_cajero, "\nbilletes 20000=", 0, "\nbilletes 10000=", 0, "\nbilletes 5000=", suma) 
            n = input()
            if n != "N" :
                break
            else:
                continue