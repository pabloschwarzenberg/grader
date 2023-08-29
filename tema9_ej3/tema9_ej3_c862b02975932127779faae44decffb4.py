def decodificar(mensaje):
    mensaje=mensaje.split(",")
    mensajedecof=[]    
    for i in mensaje:
      i=int(i,2)
      i=chr(i)
      i=str(i)
      mensajedecof.append(i)
    
    mensajedecof="".join(mensajedecof)
    return mensajedecof

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)



         