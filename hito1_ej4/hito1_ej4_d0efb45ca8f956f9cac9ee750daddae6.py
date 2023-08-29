def transformar_decimal_binario(decimal): #Aplicamos un def para definir una funcion.
    if decimal <= 0:
        return "0" #Devolvemos un 0 si el decimal es menor o igual a 0 ya que no se puede seguir dividiendo.
    binario = ""
    while decimal > 0: #Aplicamos un ciclo while para ir repitiendo el proceso de división.
        resto = int(decimal % 2) #EL % es para sacar el sobrante de una division.
        decimal = int(decimal/2) #Ahora llamamos al decimal que salió del resto y aplicamos la división.  
        binario = str(resto) + binario #Aplicamos un string para transformar a texto el resultado.
    return binario


decimal = int(input("Ingrese un número decimal:")) #Llamamos a decimal y le agregamos un int porque ingresaremos numero y input para capturar los datos ingresados.
binario = transformar_decimal_binario(decimal)
print(f"El número {decimal} es {binario} en código binario")