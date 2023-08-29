#Sistema de Ecuaciones
def sol_sis1(a, b, c, d, e, f):
    determinante = a*e - b*d
    if determinante != 0:
        x = (c*e - b*f)
        return x
    else:
        return None, None

def sol_sis2(a, b, c, d, e, f):
    determinante = a*e - b*d
    if determinante != 0:
        y = (a*f - c*d)
        return y
    else:
        return None, None



print("Digite valores coeficientes")
a, b, c, d, e, f = map(float, input().split())

print("x=",end="")
print(sol_sis1(a, b, c, d, e, f))
print("y=",end="")
print(sol_sis2(a, b, c, d, e, f))