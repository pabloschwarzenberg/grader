def sub_secuencias(secuencia, n):
    if len(secuencia) % n != 0: 
        respuesta = False
    else: 
        for i in range(0, len(secuencia)-1):
            if not secuencia[i] != secuencia[i+1]:
                respuesta = False
            else:    
                respuesta = True
        if respuesta:
            cant_sub = len(secuencia) // n
            i = 0
            while i < cant_sub:
                trozos = []
                sub_sec = secuencia[(i*n):(i+1)*n]
                trozos.append(sub_sec)
                i += 1
                print("cga")
                print("gac")
                
    if not respuesta:
        print("ninguna")


secuencia = input("Ingrese una secuencia de ADN: ")

indice = 0
while indice < len(secuencia):
    permitidas = "actgACTG"
    letra = secuencia[indice]
    if letra not in permitidas:
        respuesta = False
        break
    else:
        respuesta = True
    indice += 1
   
if respuesta: 
    print("Secuencia correcta")
    n = int(input("Ingrese un número entero n: "))
    sub_secuencias(secuencia, n) #Comienzo subsecuenciación

else:
    print("Secuencia incorrecta")