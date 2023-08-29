def decodificar(mensaje):

  def antibinario(binario):
    binario=str(binario)
    binario=binario[::-1]
    sumatoria=0
    for i in range(len(binario)):
      a=int(binario[i])*(2**i)
      sumatoria+=a
    return sumatoria

  contador=0
  numero=[]
  palabra=[]
  p = ""
  for i in range(len(mensaje)):
    if mensaje[i]!=",":
      p = p + mensaje[i]
      contador+=1
      if (contador+1)%9==0:
        numero.append(antibinario(p))
        p=""
    else:
      contador+=1
  for j in range(len(numero)):
    palabra.append(chr(numero[j]))
  palabra="".join(palabra)
  return palabra
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         