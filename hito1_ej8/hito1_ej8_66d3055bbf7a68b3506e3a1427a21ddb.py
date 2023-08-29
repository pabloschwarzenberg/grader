#Descomponer un número
numero= int(input("Ingrese el numero de no más de 4 digitos: "))
mil=(numero%10000-numero%1000)//1000
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10

if mil==0 and centenas==0 and decenas==0:
    print(str(unidades)+"U")

elif mil==0 and centenas==0:
    print(str(decenas)+"D" + "+" + str(unidades)+"U")

elif mil==0:
    print(str(centenas)+"C" + "+" + str(decenas)+"D" + "+" + str(unidades)+"U")

else:
    print((str(mil)+"M" + "+" + str(centenas)+"C" + "+" + str(decenas)+"D" + "+" + str(unidades)+"U"))    