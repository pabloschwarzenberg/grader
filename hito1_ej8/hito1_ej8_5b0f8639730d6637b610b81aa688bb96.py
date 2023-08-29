numero = int (input ('Ingresa el valor de numero: '))
miles=(numero%10000-numero%1000)//1000
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10
if 9999 >= numero >= 1000:
    print ((repr (miles))+"M+"+(repr (centenas))+"C+"+(repr (decenas))+"D+"+(repr (unidades))+"U")
elif 999 >= numero >= 100:
     print ((repr (centenas))+"C+"+(repr (decenas))+"D+"+(repr (unidades))+"U")
elif 99 >= numero >= 10:
     print ((repr (decenas))+"D+"+(repr (unidades))+"U")
elif 9 >= numero >= 0:
     print ((repr (unidades))+"U")  