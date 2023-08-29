# completa el código de la función
FloydWarshall (n, C, A) # n = número de vértices, C = matriz de costo
{ # A = matriz resultado de costo
for i in range(n):
for j in range(n):
if i ≠ j:
A[i][j] = C[i][j]
else
A[i][j] = 0
for i in range(n):
for j in range(n):
if i == j or graph[i][j] <> ∞:
path[i][j] = j
for k in range(n):
for i in range(n):
for j in range(n):
if (A[i][k] + A[k][j] < A[i][j])
A[i][j] = A[i][k] + A[k][j]
path[i][j] = path[i][k]
}