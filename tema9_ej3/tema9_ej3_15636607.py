def decodificar(mensaje):
    mensaje=mensaje.strip()
    mensaje=mensaje.split(',')
    l=len(mensaje)
    reps=[]
    for cbin in mensaje:
        chex=0
        for i in range(0,8):
            if cbin[i]=='1':
                chex=chex+(2**(7-i))
        print(chex)
        reps.append(chr(chex))
    print(reps)
    mensaje=''
    for rep in reps:
        mensaje=mensaje+str(rep)
        
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)