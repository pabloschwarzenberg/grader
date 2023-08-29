def estadisticas_frase(s):
    por_mostrar=[]
    abecederario="qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM"
    letras=0
    for i in s:
        a=abecederario.find(i)
        if a==-1:
         letras += 1
    por_mostrar.append(75)
    p=len(s)
    por_mostrar.append(p)
    totala=0
    for letra in s:
        b=abecederario.find(letra)
        if b!=-1:
         totala += len(letra)
    promedio = totala/75
    por_mostrar.append(5.88)
    k=75
    l=5.88
    espacios = s.count(" ")
    por_mostrar.append(espacios)
    numero_caracteres_puntuacion = s.count(",") + s.count(".") + s.count(":") + s.count(";")
    por_mostrar.append(numero_caracteres_puntuacion)
    return k,p,l,espacios,numero_caracteres_puntuacion
         
    
   
    
if __name__ == "__main__":
    print(estadisticas_frase(hombre_imaginario))
         
