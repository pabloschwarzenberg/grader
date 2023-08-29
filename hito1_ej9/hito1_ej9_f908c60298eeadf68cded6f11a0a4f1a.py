numero1 = int(input("Ingrese el 1N:"))
numero2 = int(input("Ingrese el 2N:"))
numero3 = int(input("Ingrese el 3N:"))
numero4 = int(input("Ingrese el 4N:"))
numero5 = int(input("Ingrese el 5N:"))
numero6 = int(input("Ingrese el 6N:"))

det = (numero1*numero5) - (numero2*numero4)

x = ((numero3*numero5) - (numero2*numero6))/det
y = ((numero1*numero6) - (numero3*numero4))/det

print("x=",x,"y=",y)
      