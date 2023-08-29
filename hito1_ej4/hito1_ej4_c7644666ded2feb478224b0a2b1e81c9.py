numero = int(input("Ingresa un número para convertir a binario: "))
mensaje = ""


while(numero > 0):

    if(numero % 2 == 0):
        mensaje += "0"
    else:
        mensaje += "1"
    numero //= 2
    
    
mensaje_final = mensaje[::-1]
print("resultado=",mensaje_final)