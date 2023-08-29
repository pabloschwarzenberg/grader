#Sistema de Ecuaciones
def solucion(num1,num2,num3,num4,num5,num6):
    det = num1*num5 - num2*num4
    if det != 0:
        x = (num3*num5 - num2*num6)/det
        y = (num1*num6 - num3*num4)/det       
        print("x=", x, "y=", y)
    else:
        return None, None

num1 = int(input("Ingrese su primer numero : "))
num2 = int(input("Ingrese su segundo numero : "))
num3 = int(input("Ingrese su tercer numero : "))
num4 = int(input("Ingrese su cuarto numero : "))
num5 = int(input("Ingrese su quinto numero : "))
num6 = int(input("Ingrese su sexto numero : "))
print(solucion(num1,num2,num3,num4,num5,num6))