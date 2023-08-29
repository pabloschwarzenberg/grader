from re import X


def solucion_ecuacion(a, b, c, d, e, f):
    division = a*e - b*d
    x = round((c*e - b*f)/division, 1)
    y = round((a*f - c*d)/division, 1)

    return "X=" + str(x)+ ", " + "y=" + str(y)


if __name__ == "__main__":
    print("Ingrese los números del sistema de ecuación lineal:")
    a, b, c, d, e, f = map(float, input().split())

    print(solucion_ecuacion(a, b, c, d, e, f))
