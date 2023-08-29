def rot13(palabra):
    resultado=""
    contador=0
    abecedario="abcdefghijklmnopqrstuvwxyz"
    for i in palabra:
      pos_letra=abecedario.find(i)
      if pos_letra<=12:
        reemplazo=pos_letra+13
      else:
        reemplazo=pos_letra-13
      resultado=resultado+abecedario[reemplazo]
    return resultado

if __name__ == "__main__":
    pass
           