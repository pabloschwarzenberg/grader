def decodificar(mensaje):
    codigo=mensaje.split(",")
    mensaje_final=[]
    for i in range(0,len(codigo)):
        decodificado=[]
        numberEx=int(codigo[i],2)
        i=float(numberEx)
        b=int(i)
        letra=chr(b)
        decodificado.append(letra)
        mensaje_final.append(decodificado)

    a=""
    for i in range(0,len(mensaje_final)):
        
        a += mensaje_final[i][0]
    return a
        

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         