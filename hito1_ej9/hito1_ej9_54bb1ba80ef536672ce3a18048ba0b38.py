#Sistema de Ecuaciones
def eliminar_x (x1,y1,r1,x2,y2,r2):
    multiploprimero1 = x2 * (x1)
    multiploprimero2 = x2 * (y1)
    multiploprimero3 = x2 * (r1)
    multiplosegundo1 = -(x1) * (x2)
    multiplosegundo2 = -(x1) * (y2)
    multiplosegundo3 = -(x1) * (r2)
    primero = multiploprimero1 + multiplosegundo1
    segundo = multiploprimero2 + multiplosegundo2
    tercero = multiploprimero3 + multiplosegundo3
    resultado = tercero / (primero + segundo)
    return resultado

def eliminar_y (x1,y1,r1,x2,y2,r2):
    multiploprimero1 = y2 * (x1)
    multiploprimero2 = y2 * (y1)
    multiploprimero3 = y2 * (r1)
    multiplosegundo1 = -(y1) * (x2)
    multiplosegundo2 = -(y1) * (y2)
    multiplosegundo3 = -(y1) * (r2)
    primero = multiploprimero1 + multiplosegundo1
    segundo = multiploprimero2 + multiplosegundo2
    tercero = multiploprimero3 + multiplosegundo3
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