def resolver_sistema(a1, b1, c1, a2, b2, c2):
    # Aplicar el método de eliminación de Gauss
    det = a1*b2 - a2*b1
    
    if det == 0:
        # El sistema no tiene solución única
        return None
    
    # Calcular los coeficientes de las soluciones
    x = (b2*c1 - b1*c2) / det
    y = (a1*c2 - a2*c1) / det
    
    return x, y

# Ejemplo de uso
sistema = resolver_sistema(2, 3, 6, 1, 2, 5)

if sistema is None:
    print("El sistema no tiene solución única")
else:
    x = round(sistema[0], 1)
    y = round(sistema[1], 1)
    print(f'x = {x}')
    print(f'y = {y}')
