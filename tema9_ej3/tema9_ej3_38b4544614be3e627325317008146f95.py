def decodificar(mensaje):
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
def binario_a_decimal(binario):

  posicion = 0

  decimal = 0

  binario = binario[::-1]

  for digito in binario:

    # Se eleva 2 a la posición actual

    multiplicador = 2**posicion

    decimal += int(digito) * multiplicador

    posicion += 1

  return decimal



def decodificar(mensaje):

     separador = ","

     separado_por_espacios = mensaje.split(separador)

     n=[]

     for i in separado_por_espacios:

          j=binario_a_decimal(i)

          n.append(j)

          #print(i,n)

     l=[]

     for i in n:

          k=chr(i)

          l.append(k)

          #print(i,l)

     o="".join(l)

     return o



#decodificar(mensaje)