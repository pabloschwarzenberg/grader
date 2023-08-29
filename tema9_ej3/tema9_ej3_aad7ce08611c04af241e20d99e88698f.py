def decodificar(mensaje):
    mensaje=mensaje.split(",")
    string=""
    for i in mensaje:
    	num=int(i, 2)
    	letra=chr(num)
    	string+=letra
    return string

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         