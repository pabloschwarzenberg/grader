# --------------
# Sistema de acuaciones
# --------------

def sistemaEcuaciones(a1,b1,c1,a2,b2,c2):
        
        # ---------
        # Si el determinante es cero, no tiene solución única.

        # ----
        #Calcular determinante
        determinante = a1 * b2 - a2 * b1


        if determinante == 0:
                return None
        
        # ---------
        # Calcular soluciones
        x = (c1 * b2 - c2 * b1) / determinante
        y = (a1 * c2 - a2 * c1) / determinante

        return x,y

        # --------------
        # Resolver el sistema
        solucion = sistemaEcuaciones(a1,b1,c1,a2,b2,c2)

        # --------------
        # Mostrar las soluciones
        if solucion is None:
                print("El sistema no tiene solución única.")
        else:
                x,y = solucion
                # --------------
                print("La solución es:")
                print("X=",round(x,1))
                print("y=",round(y,1))