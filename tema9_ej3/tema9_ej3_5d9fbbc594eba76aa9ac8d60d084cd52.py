def decodificar(mensaje):
    cadaBi = mensaje.split(",")
    listaNumeros = []
    palabra = ""
    abc = ["a","b","c","d","e","f","g","h","i","j",
           "k","l","m","n","o","p","q","r","s","t",
           "u","v","w","x","y","z"]
    num = ["97","98","99","100","101","102","103","104",
           "105","106","107","108","109","110","111","112",
           "113","114","115","116","117","118","119","120",
           "121","122"]
    for i in cadaBi:
        k = 7
        numero = 0
        for j in i:
            a = int(j)
            numero += (a*(2**k))
            k -= 1
        listaNumeros.append(numero)
    for pos1 in listaNumeros:
        for pos2 in range(len(num)):
            if str(pos1) == num[pos2]:
                palabra += abc[pos2]
    return (palabra)
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         