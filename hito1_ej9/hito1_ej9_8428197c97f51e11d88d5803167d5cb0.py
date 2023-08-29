#Sistema de Ecuaciones
 def solve_system(a1, b1, c1, a2, b2, c2):
    det = a1 * b2 - a2 * b1
    det_x = c1 * b2 - c2 * b1
    det_y = a1 * c2 - a2 * c1
    x = det_x / det
    y = det_y / det
    return x, y

a1 = 2
b1 = 3
c1 = 6
a2 = 1
b2 = 2
c2 = 5

x, y = solve_system(a1, b1, c1, a2, b2, c2)

print(f"x={x:.1f}")
print(f"y={y:.1f}")  