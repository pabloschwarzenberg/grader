numero = int(input("ingrese un numero: ")) 
binario = "" #aqui se van a reescribir los números binarios obtenidos en tipo str.
while numero > 0: #este while es para trabajar varias veces con la misma formula.
    residuo = numero % 2 
    binarioA = 0 #este binario lo usaremos para tener uno de tipo int.
    binarioA = binarioA + residuo 
    decimal = numero // 2 
    numero = decimal #el número se reemplaza por el obtenido en decimal para no entrar en un buble infinito
    if binarioA == 0: 
        binario = binario + "0"
    else:
        binario = binario + "1"
#Con esto que hare abajo ordenare los números binarios.
binario = list(binario)
binario.reverse()
binario = "".join(binario)
#aqui se mostrara el número0
print("resultado="+binario)