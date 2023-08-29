def basccii(binario):
    valor = int(binario,base =2)
    return chr(valor)
def decodificar(txbin):
    texto = ""
    for nb in txbin.split(','):
        texto += basccii(nb)
    return texto

if _name_ == "_main_":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)