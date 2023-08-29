#Sistema de Ecuaciones
def eliminar_x (x1,y1,r1,x2,y2,r2):
    multiprimer1 = x2 * (x1)
    multiprimer2 = x2 * (y1)
    multiprimer3 = x2 * (r1)
    multisegund1 = -(x1) * (x2)
    multisegund2 = -(x1) * (y2)
    multisegund3 = -(x1) * (r2)
    primero = multiprimer1 + multisegund1
    segundo = multiprimer2 + multisegund2
    tercero = multiprimer3 + multisegund3
    resultado = tercero / (primero + segundo)
    return resultado

def eliminar_y (x1,y1,r1,x2,y2,r2):
    multiprimer1 = y2 * (x1)
    multiprimer2 = y2 * (y1)
    multiprimer3 = y2 * (r1)
    multisegund1 = -(y1) * (x2)
    multisegund2 = -(y1) * (y2)
    multisegund3 = -(y1) * (r2)
    primero = multiprimer1 + multisegund1
    segundo = multiprimer2 + multisegund2
    tercero = multiprimer3 + multisegund3
    resultado = tercero / (primero + segundo)
    return resultado
x1 = float(input("primera x"))
y1 = float(input("primera y"))
r1 = float(input("primer resultado"))
x2 = float(input("segunda x"))
y2 = float(input("segunda y"))
r2 = float(input("segundo resultado"))
print("x=" + str(eliminar_y (x1,y1,r1,x2,y2,r2)))
print("y=" + str(eliminar_x (x1,y1,r1,x2,y2,r2))) 