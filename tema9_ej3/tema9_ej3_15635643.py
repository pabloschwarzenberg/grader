def decodificar(mensaje):
    caracteres=mensaje.split(",")
    traduccion=""
    nums=[]
    for seq in caracteres:
        num=int(seq,2)
        nums.append(num)
    for numero in nums:
        letra=chr(numero)
        traduccion+=letra
    return traduccion

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         