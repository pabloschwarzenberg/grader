def __mul__(self, other):
if len(self.celdas) == 0 or len(other.celdas) == 0:
return Matriz()

if len(self.celdas[0]) != len(other.celdas):
raise ValueError("Las matrices no se pueden multiplicar")

filas_self = len(self.celdas)
columnas_self = len(self.celdas[0])
columnas_other = len(other.celdas[0])

resultado = [[0 for _ in range(columnas_other)] for _ in range(filas_self)]

for i in range(filas_self):
for j in range(columnas_other):
for k in range(columnas_self):
resultado[i][j] += self.celdas[i][k] * other.celdas[k][j]

return Matriz(resultado)