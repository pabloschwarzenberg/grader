#Sistema de Ecuaciones
def det(m):
    det = ((m[0][0]) * (m[1][1]) - (m[0][1] * m[1][0]))
    return det


print("Dado el sistema de la forma: ax+by=c y dx+ey=f. define los coeficientes.")

a = float(input("Dame el valor de a:",))
b = float(input("\nDame el valor de b:",))
c = float(input("\nDame el valor de c:",))
d = float(input("\nDame el valor de d:",))
e = float(input("\nDame el valor de e:",))
f = float(input("\nDame el valor de f:",))

matriz = [[a,b],
          [d,e]]

matrizx = [[c,b],
           [f,e]]

matrizy = [[a,c],
           [d,f]]

det_sistema = det(matriz)

det_X = det(matrizx)

det_Y = det(matrizy)

x = (det_X)/(det_sistema)

y = (det_Y)/(det_sistema)

print("x = {}\ny = {}".format(round(x,1),round(y,1)))     