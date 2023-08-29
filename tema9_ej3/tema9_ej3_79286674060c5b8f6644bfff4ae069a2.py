def decodificar(mensaje):
    mensaje=mensaje.split(",")
    decimal=[]
    for i in mensaje:
        convertido_adecimal=0
        p=1
        for j in i:
            exponente=(len(i)-p)
            valor=int(j)*2**exponente
            convertido_adecimal+=valor
            p+=1
        decimal.append(convertido_adecimal)
    mensaje=decimal
    mensaje [:]=[str(chr(a)) for a in mensaje]

    mensaje="".join(mensaje)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         