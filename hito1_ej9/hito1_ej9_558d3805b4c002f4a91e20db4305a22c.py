#Sistema de Ecuaciones
a1 = int(input("Ingrese el valor A de la ecuación 1: "))
b1 = int(input("Ingrese el valor B de la ecuación 1: "))
ans_1 = int(input("Ingrese la solución de la ecuación 1: "))
a2 = int(input("Ingrese el valor A de la ecuación 2: "))
b2 = int(input("Ingrese el valor B de la ecuación 2: "))
ans_2 = int(input("Ingrese la solución de la ecuación 2: "))

a2_minus = a2 * (-2)
b2_minus = b2 * (-2)
ans2_minus = ans_2 * (-2)
new_a = a1 + a2_minus
new_b = b1 + b2_minus
new_ans = ans_1 + ans2_minus
final_y_val = round(new_ans / new_b, 1)
temp_y = b1 * final_y_val
partial_ans = ans_1 - temp_y
x_val = round(partial_ans / a1, 1)
#["x=" + str(x_val), "y=" + str(final_y_val)]

print("x=" + str(x_val), "y=" + str(final_y_val))