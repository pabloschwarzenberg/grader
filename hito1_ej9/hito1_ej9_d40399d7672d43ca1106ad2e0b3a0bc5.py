#Sistema de Ecuaciones
#Entradas
#Ecuación 1
e1_a = int(input("Ingrese número que acompaña a X: "))
e1_b = int(input("Ingrese número que acompaña a Y: "))
e1_c = int(input("Ingrese resultado de primera ecuación: "))
#Ecuación 2
e2_d = int(input("Ingrese número que acompaña a X: "))
e2_e = int(input("Ingrese número que acompaña a Y: "))
e2_f = int(input("Ingrese resultado de segunda ecuación: "))

#Procesos
det_s = (e1_a * e2_e) - (e1_b * e2_d)
det_x = (e1_c * e2_e) - (e1_b * e2_f)
det_y = (e1_a * e2_f) - (e1_c * e2_d)

x = round((det_x / det_s),1)
y = round((det_y / det_s),1)

print("x=",x)
print("y=",y) 