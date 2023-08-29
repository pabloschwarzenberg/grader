import re
def decodificar(mensaje):
    a = []
    binary = mensaje.split(',')
    for i in range(len(binary)):
        decimal = int(binary[i],2)
        letter = chr(decimal)
        a.append(letter)       
    return ''.join(a)

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         
