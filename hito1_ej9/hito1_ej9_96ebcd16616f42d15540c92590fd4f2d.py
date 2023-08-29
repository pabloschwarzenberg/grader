#Sistema de Ecuaciones
coeficiente_x1 = int(input())
coeficiente_y1 = int(input())
suma_1 = int(input())

coeficiente_x2 = int(input())
coeficiente_y2 = int(input())
suma_2 = int(input())

def resolv_sist_ecu(cx1,cy1,s1,cx2,cy2,s2):
    y = ((cx1 * s2) - (cx2 * s1))/(-(cx2 * cy1) + (cx1 * cy2))
    
    x = (s1 - (cy1 * y))/ cx1
    
    return x, y
    
x, y = resolv_sist_ecu(coeficiente_x1, coeficiente_y1, suma_1, coeficiente_x2, coeficiente_y2, suma_2)

print("x={}".format(x))
print("y={}".format(y))
