#Conversión de Decimal a Binario
#Definir función para eld ecimal de entrada:
def convertir(decimal):
    if decimal == 0:
        return '0'
    #Porque cero en decimal es igual a cero en binario xd
    binario = '' 
    #Cadena de caracteres vacía, donde se almacenará el valor del decimal convertido
    while decimal > 0:
        #El modulo (%) calcula el residuo (números después de la coma) de la división 
        residuo = decimal % 2
        binario = str(residuo) + binario #Concatena el valor de residuo, sin sumar los valores, uniéndolos en orden
        #Después del signo + da vuelta el número binario para que quede en el orden correcto
        decimal = decimal // 2 #División considerando solo enteros
      return binario
#Uso
d = int(input("Ingrese un número en entero en el sistema decimal: "))
resultado = convertir(d)
print("El número binario correspondiente es: ", resultado)