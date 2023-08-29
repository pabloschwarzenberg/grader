#Sistema de Ecuaciones
def solution_sistem(a, b, c, d, e, f):
    determinante = a*e - b*d
    
    if determinante != 0:
        x = (c*e - b*f) / determinante
        y = (a*f - c*d) / determinante

        return x, y
    else:
        return None, None

    
print("Digite los valores para a,b,c,d,e y f : ")
a, b, c, d, e, f = list(map(float, input().split()))

print(solution_sistem(a, b, c, d, e, f))