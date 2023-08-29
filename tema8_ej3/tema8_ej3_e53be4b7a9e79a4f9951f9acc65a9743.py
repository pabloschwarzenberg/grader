def estadisticas_frase(frase):
    num_crt = 0
    num_crt_esp = 0
    num_Epcio = 0
    num_palabras = 0
    largoPromedio = 0  
    for i in frase:        
        num_crt += 1           
        if i == '.' or i == ',':
            num_crt_esp += 1
        if  i == ' ':
            num_Epcio += 1
    frase = frase.replace('\n', ' ')
    frase = frase.replace('.', '')
    texto = frase.split()
    while num_palabras < len(texto):
        palabra = texto[num_palabras]
        num_palabras+=1
    cont = []
    for palabra in texto:
        x = len(palabra)
        cont.append(x)
    largoPromedio = sum(cont)/num_palabras
    return num_palabras, num_crt, largoPromedio, num_Epcio, num_crt_esp       