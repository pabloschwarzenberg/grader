def decodificar(mensaje):
    mensaje=mensaje+","
    indice=0
    string=""
    n=0
    while indice<len(mensaje):
        longitud = 7
        suma = 0
        if mensaje[indice]==",":
            sub_string=mensaje[n:indice]
            for j in sub_string:
                j=int(j)
                multi=int((2**longitud)*j)
                suma=suma+multi
                longitud=longitud-1
            letra = chr(suma)
            string=string+letra
            n=indice+1
        indice+=1
    return string

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         