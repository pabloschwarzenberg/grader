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