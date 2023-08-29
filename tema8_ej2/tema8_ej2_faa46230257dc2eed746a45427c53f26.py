def buscarTodas(a,b):
    indices = ""
    numero = 0
    for i in a:
      numerostr = str(numero)
      if i == b:
        if indices == "":
          indices += numerostr
        else:
          indices += " "
          indices += numerostr
      numero +=1

    return indices

