numero = int (input ('Ingresa el valor de numero: '))
milesimas=(numero%10000-numero%1000)//1000
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10

milesimas=str(milesimas)
centenas=str(centenas)
decenas=str(decenas)
unidades=str(unidades)

m="M"
c="C"
d="D"
u="U"
milesimas= milesimas+m
centenas= centenas+c
decenas= decenas+d
unidades= unidades+u



print(milesimas,"+",centenas,"+",decenas,"+",unidades)