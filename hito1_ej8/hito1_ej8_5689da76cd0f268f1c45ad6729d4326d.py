numero= int(input("Ingresar Numero:   "))

numero1= (numero%10)
numero2= (numero%100)
numero2a= (numero2//10)
numero3= (numero%1000)
numero3a=(numero3//100)
numero4= (numero%10000)
numero4a=(numero4//1000)




print ((str(numero4a)+("M+"))+(str(numero3a)+("C+"))+(str(numero2a)+("D+"))+(str(numero1)+("U")))

