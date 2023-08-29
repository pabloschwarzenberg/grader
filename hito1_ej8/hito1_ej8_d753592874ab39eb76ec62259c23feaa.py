#Descomponer un número
#Numero=int(input("Ingrese el númros a descomponer:"))
a=0


unidades_totales=int(input("Ingrese el número a descomponer: "))
Miles=unidades_totales//1000
#print(Miles,"mil")
Centenas=(unidades_totales%1000)//100
#print(Centenas,"centenas")
Decenas=(unidades_totales%100)//10
#print(Decenas,"Decenas")
Unidades=unidades_totales%10
#print(Unidades, "unidades")
print( Miles,"M+", Centenas, "C+", Decenas, "D+", Unidades, "U")
