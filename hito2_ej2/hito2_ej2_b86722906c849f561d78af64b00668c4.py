secuencia = input("Escriba una secuencia: ")


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
else:
    print("Secuencia incorrecta")
 