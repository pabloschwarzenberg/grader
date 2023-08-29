print ("Introduce el número:")
numero = int(input())

umil = numero // 1000
tmp = numero % 1000

centenas = tmp // 100
tmp = tmp % 100

decenas = tmp // 10
unidades = tmp % 10
if umil!=0:
    print ("{}M+{}C+{}D+{}U".format(umil,centenas,decenas,unidades))
elif centenas!=0:
    print ("{}C+{}D+{}U".format(centenas,decenas,unidades))
elif decenas!=0:
    print ("{}D+{}U".format(decenas,unidades))
elif unidades!=0:
    print ("{}U".format(unidades))