#Conversión de Decimal a Binario
#primero defino la función
def tran_binario(numero):
    a = ""
    while (numero // 2) != 0:
    #La división debe ser distinta de cero para seguir determinando las cifras del binario 
        a = str(numero%2)+ a
        numero = numero//2
        
    return str(numero)+ a


numero = int(input("Ingrese un número: "))
print("resultado=", tran_binario(numero))
     