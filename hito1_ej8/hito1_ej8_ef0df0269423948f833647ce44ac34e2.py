#Descomponer un número
numero= int(input("Ingrese numero: "))

def descomponer(numero):
    if numero>9999:
        print ("no se puede ingresar numero de 5 digitos")
        return

    a= ""
    if numero>=1000:
        miles= numero//1000
        a= a+str(miles)+ "M +"
        centenas = (numero%1000) // 100
        a = a + str(centenas) + "C +"
        decenas = (numero%100) // 10
        a = a + str(decenas) + "D +"
        unidades = (numero%10) // 1
        a = a + str(unidades) + "U "

    if numero>=100 and numero<1000:
        centenas= numero//100
        a= a+str(centenas)+ "C +"
        decenas = (numero%100) // 10
        a = a + str(decenas) + "D +"
        unidades = (numero%10) // 1
        a = a + str(unidades) + "U "

    if numero>=10 and numero<100:
        decenas= numero//10
        a= a+str(decenas)+ "D +"
        unidades = (numero%10) // 1
        a = a + str (unidades) + "U "

    if numero>=1 and numero<10:
        unidades= numero//1
        a= a+str(unidades)+ "U "

    print (a)

descomponer(numero)