def bin_a_dec(mensaje):
    decimales=[]
    contador=0
    mensaje=mensaje.split(",")
    for i in range(len(mensaje)):
        for j in range(8):
          if mensaje[i][j]=="1":
              contador+=2**(8-(j+1))
          else:
              contador+=0
        decimales.append(contador)
        contador=0
    return decimales

def decodificar(mensaje):
    texto=bin_a_dec(mensaje)
    resp=[]
    for letra in texto:
        resp.append(chr(letra))
    mensaje="".join(resp) 
    return mensaje

if __name__ == "__main__":
    decodificar(mensaje)
    print(mensaje)