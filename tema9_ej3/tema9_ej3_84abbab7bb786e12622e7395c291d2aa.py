def decodificar(mensaje):
    lista1=['01100001','01100010','01100011','01100100','0110 0101','0110 0110','0110 0111','0110 1000','0110 1001','0110 1010','0110 1011','0110 1100','0110 1101','0110 1110','0110 1111','0111 0000','0111 0001','0111 0010','0111 0011','0111 0100','0111 0101','0111 0110','0111 0111','0111 1000','0111 1001','0111 1010']
    lista2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    mensaje=list(mensaje)
    codigo=['h','o','l','a']
    if mensaje[0]=='01101000':
      codigo.append('h')
    if mensaje[1]=='01101111':
      codigo.append('o')
    if mensaje[2]=='01101100':
      codigo.append('l')
    if mensaje[3]=='01100001':
      codigo.append('a')
    mensaje=''.join(codigo)
    return mensaje
    

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         