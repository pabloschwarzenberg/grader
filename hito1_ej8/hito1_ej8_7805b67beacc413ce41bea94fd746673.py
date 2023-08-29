#Descomponer un número
numero = int(input("Ingresa entero de 4 cifras: "))
unidademil= numero//1000
centenas= (numero%1000)//100
decena=(numero%100)//10
unidades= numero%10

mensaje = str(unidademil)+"M + " + str(centenas)+"C + " + str(decena) + "D + " + str(unidades) + "U"

print(mensaje)      