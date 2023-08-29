def decodificar(mensaje):
    cod=list(mensaje.split(","))
    palabra=""
    for i in cod:
        num=0
        for y in range(len(i)):
            if ( (i[len(i)-y-1]) =="1"):
                num=num+pow(2,y)
        palabra=palabra+chr(num)
    return(palabra)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         