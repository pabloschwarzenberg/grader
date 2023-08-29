#Sistema de Ecuaciones
import numpy as np
n1 = float( input("Ingresa nro 1: ") )
n2 = float( input("Ingresa nro 2: ") )
n3 = float( input("Ingresa nro 3: ") )
n4 = float( input("Ingresa nro 4: ") )
n5 = float( input("Ingresa nro 5: ") )
n6 = float( input("Ingresa nro 6: ") )

A = np.array([
    [n1, n2],
    [n4, n5]
])
b = np.array([n3, n6])
x = np.linalg.solve(A, b)

print( 'x={}'.format( round(x[0], 1) ) )
print( 'y={}'.format( round(x[1], 1) ) )
