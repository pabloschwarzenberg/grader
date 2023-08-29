mensaje = "01101000,01101111,01101100,01100001"

def decodificar(mensaje):
    def pasarBinario(mensaje):
        digito = int(mensaje,2)
        return chr(digito)
    def crearStr(mensaje):
        palabra = ""
        for binario in mensaje.split(","):
            palabra += pasarBinario(binario)
        return palabra
    return crearStr(mensaje)
