def decodificar(mensaje):
    potencias_2=[128,64,32,16,8,4,2,1]
    mensaje=mensaje.split(",")
    chr_s=[]
    decodificado=[]
    for i in range(0,len(mensaje)):
        suma=0
        for j in range(0,8):
            if mensaje[i]=="0100000":
                suma=32
            else:
                suma=int(suma+int(int(mensaje[i][j])*potencias_2[j]))
        chr_s.append(suma)
    for k in range(0,len(chr_s)):
        decodificado.append(chr(chr_s[k]))  
    mensaje="".join(decodificado)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         