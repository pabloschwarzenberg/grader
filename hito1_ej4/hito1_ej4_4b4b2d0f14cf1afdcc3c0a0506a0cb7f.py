#Conversión de Decimal a Binario
      mport math

n = int(input("ingrese número para el factorial: "))

if n >= 0:

    if (n >0):

        y=math.factorial(n)

        print("El factorial del número",n ,"coresponde a",y) 

    else:

        print("el factorial de cero es 1")

else:

    print("no se puede calcular factorial")