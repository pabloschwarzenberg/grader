# Entrada de Notas
PT = float(input( "Ingrese nota tareas: " ))
PI =  float(input( "Ingrese nota interrogaciones: " ))
NE =  float(input( "Ingrese nota examen: " ))
PP = float(input ( "Ingrese nota presentacion: " ))

# Calculo de Promedio Final
nota = 0.3 * PT + 0.3 * PI + 0.3 * NE + 0.1 * PP

# Resultado de Promedio Final
print ( "El Promedio Final es :)" , nota)