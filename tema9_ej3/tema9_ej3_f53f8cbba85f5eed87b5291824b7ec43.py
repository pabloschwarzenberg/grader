def decodificar(mensaje):
    def otra_cosa(mensaje):
        x=[]
        for i in mensaje:
            if i !=",":
                x.append(i)
        return(x)
    x=otra_cosa(mensaje)
    z=''
    for i in x:
        z+=i
    return"".join(chr(int(z[i*8:i*8+8],2))for i in range(len(z)//8))

if __name__ == "__main__":
    mensaje=decodificar("011010000,11011110,11011000,1100001")
    print(mensaje)
         