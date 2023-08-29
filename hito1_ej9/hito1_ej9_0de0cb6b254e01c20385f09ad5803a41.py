numero1 = int(input("Ingrese el primer numero "))
numero2 = int(input("Ingrese el segundo numero "))
numero3 = int(input("Ingrese el tercer numero "))
numero4 = int(input("Ingrese el cuarto numero "))
numero5 = int(input("Ingrese el quinto numero "))
numero6 = int(input("Ingrese el sexto numero "))

det = (numero1*numero5) - (numero2*numero4)

x = ((numero3*numero5) - (numero2*numero6))/det
y = ((numero1*numero6) - (numero3*numero4))/det

print("x=",x,"y=",y)