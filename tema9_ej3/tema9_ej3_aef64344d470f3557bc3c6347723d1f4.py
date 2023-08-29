def decodificar(mensaje):
    binario=[128,64,32,16,8,4,2,1]
    hi=mensaje.split(",")
    suma=0
    h=0
    his=[]
    for i in hi:
        h=0
        suma=0
        for j in i:
            if j=="1":
              suma+=binario[h]
            h+=1
        his.append(suma)
    mensaje=""
    for i in his:
        mensaje+=chr(i)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         