def subsecuencia(string,entero):
    string=string.lower()
    ubicacion=[]
    for i in range(0,len(string)-2):
        palabra=string[i:entero+i]
        ubicacion.append(palabra)
    final=[]
    for t in ubicacion:
        if ubicacion.count(t)==1:
            final.append(t)

    if len(final)==0:
        final.append("Ninguna")

    return final

string=input("Ingrese secuencia de adn:")
entero=int(input("Ingrese numero del largo de las subsecuencias:"))
print(subsecuencia(string,entero))

