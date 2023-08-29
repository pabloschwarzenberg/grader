def decodificar(mensaje):
    s=""
    a=mensaje.split(",")
    for i in a:
        numero=int(i)
        mult = 0 #2**0, 2**1, 2**2, ... 2**7
        contador = 0 #0.... 7 ==> 8
        suma = 0
        while numero != 0:
            digito  = numero%10
            suma+= digito*(2**mult)
            mult+=1
            contador+=1
            if contador==8:
                print(suma)
                contador=0
                mult = 0
                suma = 0

            numero = numero//10

        s=s+chr(suma)
    return(s)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         