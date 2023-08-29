# por favor escribe aquí tu función
def es_primo(numero):
  s1 = []
  for i in range(numero) :
                if(numero%(i+1) == 0) :
                        s1.append(i+1)
                i = i + 1
  if(len(s1) == 2) : es = True
  else : es = False
  return(es)
           