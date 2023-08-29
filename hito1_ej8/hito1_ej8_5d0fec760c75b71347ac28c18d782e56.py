#Descomponer un número
 print("DESCOMPONEDOR DE NUMEROS (hasta 4 digitos)")
numero = int(input("Ingrese un nunero a ser descompuesto: "))

if 0<=numero<=9:
    print(numero,"U")
    
elif 10<=numero<=99:
    unidad = numero%10
    decena = numero//10
    print(str(decena)+str("D"),str("+"),str(unidad)+str("U"))

elif 100<=numero<=999:
    unidad = numero%10
    decena = (numero//10)%10
    centena = numero//100
    print(str(centena)+str("C"),str("+"),str(decena)+str("D"),str("+"),str(unidad)+str("U"))

elif 1000<=numero<=9999:
    unidad = numero%10
    decena = (numero//10)%10
    centena = (numero//100)%10
    miles = numero//1000
    print (str(miles)+str("M"),str("+"),str(centena)+str("C"),str("+"),str(decena)+str("D"),str("+"),str(unidad)+str("U"))

else:
    print("Numero ingresado no valido")
         