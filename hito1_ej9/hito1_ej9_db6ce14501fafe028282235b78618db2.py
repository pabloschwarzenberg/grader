#Sistema de Ecuaciones
def result(determinants):
    x = determinants[1] / determinants[0]
    y = determinants[2] / determinants[0]
    return [x, y]

def determinant(matrix):
    d = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    dx = matrix[0][2] * matrix[1][1] - matrix[0][1] * matrix[1][2]
    dy = matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0]
    return [d, dx, dy]

def matrix(a, b):
    M = [a[0], a[1], a[2], b[0], b[1], b[2]]
    M = [M[:3], M[3:]]
    return M

def main():
    print('Función para resolver ecuaciones de dos variables')
    print('Ingrese los valores de la ecuación 1')
    equation1 = getData()
    print('Ingrese los valores de la ecuación 2')
    equation2 = getData()
    resulte = result(determinant(matrix(equation1, equation2)))

    print("El resultado de las variables es:")
    print("x =", round(resulte[0], 1))
    print("y =", round(resulte[1], 1))

def getData():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    return [a, b, c]

if __name__ == '__main__':
    main()

