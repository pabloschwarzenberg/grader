#Descomponer un número
numero = int(input("Introduce el número: "))



umil = numero / 1000
tmp = numero % 1000

centenas = tmp / 100
tmp = tmp % 100

decenas = tmp / 10
unidades = tmp % 10


finalum = ("%iM" % umil)
finalc= ( "%iC" % centenas   )
finald = ("%iD" % decenas)
finalu = ("%iU" % unidades)
if finalum == "0M" and finalc =="0C" and finald == "0D":
    print("{}".format(finalu))
elif finalum == "0M" and finalc =="0C":
    print("{}+{}".format(finald, finalu))
elif finalum == "0M" :
    print("{}+{}+{}".format(finalc, finald, finalu))
else:
    print("{}+{}+{}+{}".format(finalum, finalc, finald, finalu))

     