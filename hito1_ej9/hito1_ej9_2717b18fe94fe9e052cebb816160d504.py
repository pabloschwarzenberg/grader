#Sistema de Ecuaciones
      
def eq_sys(a, b, c, d, e, f):
	det = a*e - b*d

	if(det != 0):
		x = (c * e - b * f) / det
		y = (a * f - c * d) / det

		return x, y
	else:
		return None, None

print("ax + by = c \ndx + ey = f\n\n")


a, b, c, d, e, f = map(float, input("Ingrese los valores para a, b, c, d, e y f: ").split())
print(eq_sys(a, b, c, d, e, f))