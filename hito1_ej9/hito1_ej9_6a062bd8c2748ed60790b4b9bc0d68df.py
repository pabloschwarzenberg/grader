def resolver_sistema(a1, b1, c1, a2, b2, c2):
    determinante = a1 * b2 - a2 * b1
    
    if determinante == 0:
        print("El sistema no tiene solución.")
        return
    
    x = (c1 * b2 - c2 * b1) / determinante
    y = (a1 * c2 - a2 * c1) / determinante
    
    print("x =", round(x, 1))
    print("y =", round(y, 1))

if __name__ == "__main__":
    a1, b1, c1, a2, b2, c2 = map(float, input().split())
    
    resolver_sistema(a1, b1, c1, a2, b2, c2)
