def buscarTodas(m,n):
    indices=""
    num=0
    for i in m:
      num_str=str(num)
      if i == n:
        if indices=="":
          indices=indices+num_str
        else:
          indices=indices+" "
          indices=indices+num_str
      num=num+1
    return indices
