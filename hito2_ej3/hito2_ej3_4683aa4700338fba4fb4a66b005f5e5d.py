def encontrar_substring(secuencia, n):

    frecuencia = {}

    for i in range(0,len(secuencia), n):
        substring = secuencia[i:i+n]
        if substring in list(frecuencia.keys()):
            frecuencia[substring] += 1
        
        else:
            frecuencia[substring] = 1

    if len(frecuencia.items()) == 0:
        print('ninguna')
        return -1

    resultado = [elem for elem in frecuencia.keys() if frecuencia[elem] == 1 and len(elem) == n]
    print(resultado)
    return 0
secuencia = input()
n = int(input())

encontrar_substring(secuencia, n)