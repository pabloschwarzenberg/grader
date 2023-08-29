def binario_a_ascii(binario):
valor = int(binario, 2)
return chr(valor)
def decodificar(mensaje):
mensaje = ""
for binario in mensaje():
texto_plano += binario_a_ascii(binario)

    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         