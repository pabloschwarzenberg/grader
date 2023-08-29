separador = " "  
def binario_a_ascii(binario):
    valor = int(binario,2)
    return chr(valor)
    
def decodificar1(texto_binario):
    texto_plano = ""
    for binario in texto_binario.split(separador):
        texto_plano += binario_a_ascii(binario)
    return texto_plano

def decodificar(b):
  pala=""
  f=b.strip("'")
  a=f.split(",")
  i=0
  for i in range(len(a)):
    pal=(decodificar1(a[i]))
    pala+=pal
  return pala

if __name__ == "__main__":
    b=input()
    print(decodificar(b))
         