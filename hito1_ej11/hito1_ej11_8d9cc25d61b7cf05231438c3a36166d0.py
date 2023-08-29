#Cajero Automático
def veintemil(retira, num):
    if (retira - 20000) >= 0 and num <20:
        retira = retira - 20000
        num += 1
        return veintemil(retira,num)
    else:
        print("Billetes de 20000 = {}".format(num))
        return retira
def diezmil(retira, num):
    if (retira - 10000 ) >= 0 and num <40:
        retira = retira - 10000
        num += 1
        return diezmil(retira,num)
    else:
        print("Billetes de 10000 = {}".format(num))
        return retira
def cincomil(retira, num):
    if (retira - 5000 ) >= 0 and num <40:
        retira = retira - 5000
        num += 1
        return cincomil(retira,num)
    else:
        print("Billetes de 5000 = {}".format(num))
        return retira


intentos = 3
clave = 1803
r =10334151
while(intentos  != 0):
    veinte = [20,20000]
    diez = [40,10000]
    cinco = [40,5000]
    rut = (input("Ingrese rut: "))
    cl = int(input("Ingrese clave: "))
    if(cl == clave and r == rut):
        saldocuenta = 100000
        retira = int(input("Indique el monto a retirar: "))
        if retira <1000000:
            if(retira - 20000) >= 0:
                retira = veintemil(retira,0)
                veinte[0] = veinte[0]-retira
            if(retira - 10000) >= 0:
                retira = diezmil(retira,0)
                diez[0] = diez[0] - retira
            if(retira -5000) >=0:
                retira = cincomil(retira,0)
                cinco[0] = cinco[0] - retira
        else:
            print("Monto no permitido")

    else:
        intentos -= 1
        print("Le quedan {} intentos".format(intentos))

if(intentos == 0):
    print("Tarjeta Bloqueada")