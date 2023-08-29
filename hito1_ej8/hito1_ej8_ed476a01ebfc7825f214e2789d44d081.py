numero = int(input("Ingrese un número de máx 4 cifras: "))

if numero//1000>0 :
    milesimas = numero//1000
elif numero//1000 == 0 :
    milesimas = 0
if numero//100>=10 :
    centenas1 = numero - milesimas*1000
    centenas = centenas1//100
elif numero//100<10 :
    centenas = numero//100
else:
    centenas = 0
if numero%100>=10 :
    decenas1 = numero%100
    decenas = decenas1//10
else:
    decenas = 0

unidades = numero%10

if milesimas>0 :
    print(milesimas,'M',"+",centenas,'C',"+", decenas,'D',"+",unidades,'U', sep='')
elif milesimas == 0 and centenas>0 :
    print(centenas,'C',"+",decenas,'D',"+",unidades,'U', sep='')
elif milesimas == 0 and centenas == 0 and decenas>0 :
    print(decenas,'D',"+",unidades,'U',sep='')
elif milesimas == 0 and centenas == 0 and decenas == 0 and unidades>0:
    print(unidades,'U', sep='')
