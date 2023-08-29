#Descomponer un número
numero = int(input("ingresa un número de hasta 4 cifras: "))
respaldo = numero

digito_1 = numero%10
numero = numero//10

digito_2 = numero%10
numero = numero//10

digito_3 = numero%10
numero = numero//10

digito_4 = numero%10
numero = numero//10

if 0 <= respaldo <10:
    cadenaderespuesta = str(digito_1) + "U"

if 10 <= respaldo <100:
    cadenaderespuesta = str(digito_2)+ "D + " + str(digito_1) + "U"
    
    
if 100 <= respaldo <1000:
    cadenaderespuesta = str(digito_3)+"C + "  + str(digito_2) + "D + " + str(digito_1) +"U"
    
    
if 1000 <= respaldo <10000:
    cadenaderespuesta = str(digito_4)+"M + " + str(digito_3)+ "C + " + str(digito_2)+ "D + " + str(digito_1) + "U"

print(cadenaderespuesta)