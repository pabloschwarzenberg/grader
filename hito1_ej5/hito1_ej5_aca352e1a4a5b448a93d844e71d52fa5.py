
# Algoritmo para obtener el DV de un rut.

# Inicializa variables.
valor_entrada = int(input("Ingrese numero rut sin DV : "))
valor_invertido = ""
suma = 0
divisor = len(str(valor_entrada))
factor = 2

# Itera para invertir el orden de los caracteres.
for i in str(valor_entrada):
    valor_invertido = str(i) + valor_invertido
    

# Itera para multiplicar los valores por factor +1.
for i in str(valor_invertido):

    if factor > 7:
        factor = 2

    suma = suma + (factor * int(i) )
    factor =factor + 1

# Aplica calculos finales.
respuesta = str( 11 - (suma - (suma//11) * 11 )   ) 

if respuesta == "11" :
    respuesta = "0"
elif respuesta == "10":
    respuesta = "K"

print("dv="+respuesta)
