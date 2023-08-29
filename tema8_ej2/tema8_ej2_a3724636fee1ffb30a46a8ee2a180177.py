def buscarTodas(a,b):
    indices = ""
    num = 0
    for i in a:
      numstr = str(num)
      if i == b:
        if indices == "": 
          indices += numstr
        else:
          indices += " "
          indices += numstr
      num += 1
    return indices


     
