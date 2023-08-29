#Sistema de Ecuaciones
def eliminar_x (x1,y1,r1,x2,y2,r2):
    multy1 = x2 * (x1)
    multy2 = x2 * (y1)
    multy3 = x2 * (r1)
    ply1 = -(x1) * (x2)
    ply2 = -(x1) * (y2)
    ply3 = -(x1) * (r2)
    first = multy1 + ply1
    second = multy2 + ply2
    third = multy3 + ply3
    result = third / (first + second)
    return result

def eliminar_y (x1,y1,r1,x2,y2,r2):
    multy1 = y2 * (x1)
    multy2 = y2 * (y1)
    multy3 = y2 * (r1)
    ply1 = -(y1) * (x2)
    ply2 = -(y1) * (y2)
    ply3 = -(y1) * (r2)
    first = multy1 + ply1
    second = multy2 + ply2
    third = multy3 + ply3
    result = third / (first + second)
    return result
x1 = float(input("Primera x"))
y1 = float(input("Primera y"))
r1 = float(input("Primer resultado: "))
x2 = float(input("Segunda x"))
y2 = float(input("Segunda y"))
r2 = float(input("Segundo resultado: "))
print("x=" + str(eliminar_y (x1,y1,r1,x2,y2,r2)))
print("y=" + str(eliminar_x (x1,y1,r1,x2,y2,r2)))