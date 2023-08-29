def decodificar(mensaje):
    mensaje_l=mensaje.split(",")
    meddelande=""
    for palabra in mensaje_l:
        palabra=palabra[::-1]
        suma=0
        t=0
        while t<len(palabra):
            if palabra[t]=="1":
                delsumma=2**t
                suma+=delsumma
            t+=1
        meddelande+=chr(suma)                      
    return meddelande

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
