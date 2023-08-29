def binario_a_decimal(binario):
  posicion = 0
  decimal = 0
  binario = binario[::-1]
  for digito in binario:
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
     l=[]
     for i in n:
          k=chr(i)
          l.append(k)
 
     o="".join(l)
     return o