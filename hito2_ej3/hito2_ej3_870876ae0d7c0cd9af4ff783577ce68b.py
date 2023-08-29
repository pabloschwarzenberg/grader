def deteccion_codones_adn(secuencia,n):
    codones = []
    if len(secuencia)%n == 0 and len(secuencia) >= n:
        counter = 0
        while counter + 3 < len(secuencia)+1:
            codones.append(secuencia[counter:counter+3])
            counter = counter+3
        return print(*codones, sep = ' ')
    else:
        return print('ninguna')
secuencia = str(input())
n = int(input())
deteccion_codones_adn(secuencia,n)

