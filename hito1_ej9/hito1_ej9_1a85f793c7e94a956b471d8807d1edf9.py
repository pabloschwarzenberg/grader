def resolver_sistema():
    # Solicitar los valores del sistema por teclado
    print("Ingrese los coeficientes del sistema de ecuaciones:")
    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))
    d = float(input("d: "))
    e = float(input("e: "))
    f = float(input("f: "))
    
    determinante = a * e - b * d
    
    if determinante == 0:
        # El sistema no tiene solución única
        print("El sistema no tiene solución única.")
        return
    
    x = (c * e - b * f) / determinante
    y = (a * f - c * d) / determinante
    
    # Imprimir las soluciones redondeadas a un decimal
    print("x = {:.1f}".format(round(x, 1)))
    print("y = {:.1f}".format(round(y, 1)))

# Ejecutar la función para resolver el sistema
resolver_sistema()
