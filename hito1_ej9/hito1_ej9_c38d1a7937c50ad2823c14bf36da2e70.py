#Sistema de Ecuaciones
def sistema_ecuaciones(a, b, c, d, e, f):
    validar = a*e - b*d
    if validar != 0:
        x = (c*e - b*f) / validar
        y = (a*f - c*d) / validar
        round(x, 1)
        round(y, 1)
        return print("[","x=",x,"y=",y,"]")
    else:
        return print("No tiene solucion")
print("Digite los valores enteros de la ecuacion separados por espacio: ")
a, b, c, d, e, f = map(float, input().split())
print(sistema_ecuaciones(a, b, c, d, e, f))


      