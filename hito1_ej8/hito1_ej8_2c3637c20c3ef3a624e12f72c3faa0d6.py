#Descomponer un número
numero = int (input ('Ingresa el valor de numero: '))
milesimas=(numero%10000-numero%1000)//1000
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10
print(str(milesimas)+"M""+"+ str(centenas) +"C""+"+ str(decenas) +"D""+" + str(unidades) + "U")

