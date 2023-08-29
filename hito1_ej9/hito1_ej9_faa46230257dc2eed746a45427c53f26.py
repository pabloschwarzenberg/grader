#Sistema de Ecuaciones
numero1 = int(input("ingrese un numero: "))
numero2 = int(input("ingrese un numero: "))
numero3 = int(input("ingrese un numero: "))
numero4 = int(input("ingrese un numero: "))
numero5 = int(input("ingrese un numero: "))
numero6 = int(input("ingrese un numero: "))

y = ((numero6*numero1)-(numero4*numero3))/((numero1*numero5)-(numero4*numero2))

x = (numero3-numero2*y)/numero1

y = round(y,1)
x = round(x,1)

print("['x=",x,", 'y=",y,"']")     