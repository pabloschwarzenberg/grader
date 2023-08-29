#Sistema de Ecuaciones
def sistema_ecuaciones (pa_a, pa_b, pa_c, pa_d, pa_e, pa_f):
    var_validaSolucionable = pa_a * pa_e - pa_b * pa_d #Si el resultado es != 0, entonces tiene solución.
    if var_validaSolucionable != 0:
        var_x = (pa_c * pa_e - pa_b * pa_f) / var_validaSolucionable
        var_y = (pa_a * pa_f - pa_c * pa_d) / var_validaSolucionable
        #print("x=" + str(var_x))
        #print("y=" + str(var_y))
        return var_x, var_y
    else:
        return None,None
print("Ingrese los valores para el sistema de ecuaciones: ")
var_A = float(input())
var_B = float(input())
var_C = float(input())
var_D = float(input())
var_E = float(input())
var_F = float(input())
var_ResultadoX, var_ResultadoY = sistema_ecuaciones(var_A, var_B, var_C, var_D, var_E, var_F)
print("x=" + str(var_ResultadoX))
print("y=" + str(var_ResultadoY))