decimal = float(input("Ingresa un número decimal: "))

entero = int(decimal)  
fraccionario = decimal - entero  

parte_entera_binaria = bin(abs(entero))[2:]  


parte_fraccionaria_binaria = ""
while fraccionario != 0:
    fraccionario *= 2
    bit = int(fraccionario)
    parte_fraccionaria_binaria += str(bit)
    fraccionario -= bit

resultado = parte_entera_binaria +parte_fraccionaria_binaria

print("resultado=", resultado)

