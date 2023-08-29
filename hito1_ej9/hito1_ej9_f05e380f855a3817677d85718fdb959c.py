#Sistema de Ecuaciones
def ecuacion(num1,num2,num3,num4,num5,num6):
    determinante= (num1*num5) - (num2*num4)
    if determinante != 0:
        x = (num3*num5 - num2*num6)/determinante
        y = (num1*num6 - num3*num4)/determinante
        return print("['x=",x,"']",",","['y=",y,"']")
    else:
        return print("No tiene solución")

print("Ingrese valores para el sistema de ecuaciones ")
num1=int(input("Ingrese el primer valor para la primera ecuación: "))
num2=int(input("Ingrese el segundo valor para la primera ecuación: "))
num3=int(input("Ingrese el resultado de la primera ecuación: "))
num4=int(input("Ingrese el primer valor para la segunda ecuación: "))
num5=int(input("Ingrese el segundo valor para la segunda ecuación: "))
num6=int(input("Ingrese el resultado de la segunda ecuación: "))
print(ecuacion(num1,num2,num3,num4,num5,num6))

