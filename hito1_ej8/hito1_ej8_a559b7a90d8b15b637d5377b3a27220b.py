#Descomponer un número

número = int(input("Ingrese un númeero de maximo 4 digitos: "))
Miles = número//1000
Centena = número%1000//100
Decena = número%100//10
Unidad = número%10

#Condiciones

if número >=1 and número <=9:
    print(str(Unidad)+ "U")
if número >=10 and número <= 99:
    print(str(Decena)+ "D" + "+" + str(Unidad)+ "U")
if número >= 100 and número <= 999:
    print( str(Centena) +"C" + "+" + str(Decena)+ "D" + "+" + str(Unidad)+ "U")
if número >= 1000 and número <= 9999:
     print( str(Miles) +"M" + "+" + str(Centena) +"C" + "+" + str(Decena)+ "D" + "+" + str(Unidad)+ "U")


      