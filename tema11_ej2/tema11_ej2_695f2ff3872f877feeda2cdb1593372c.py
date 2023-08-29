def suma (x,y):
    suma = x+y
    return suma

def resta(x,y):
    resta = x-y
    return resta

def operaciones_matematicas(x,y):
    operaciones = suma(x,y)
    if operaciones == resta(x,y) or suma(x,y):
        return operaciones

def posibles_expresiones(natural1,natural2):
    if natural1 > 0 and natural2 >0 :
        expresion = str(operaciones_matematicas(natural1,natural2))
        return expresion
    else:
        print("La expresion no tiene numeros naturales")
        return

def validar_expresion(expresion):
    natural1 = int(input())
    natural2 = int(input())
    if natural1 > 0 and natural2 > 0:
        if expresion == str(operaciones_matematicas(natural1,natural2)):
            return expresion
        else:
            return validar_expresion(expresion)
