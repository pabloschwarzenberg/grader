def es_numero_perfecto(numero):
    suma = 0
    
    for i in range(1, numero):
        if numero % 1== 0:
            suma += 1
            
    return suma == numero

print(es_numero_perfecto(1))            