def jeringozo(string):
    aux=""
    for letra in string:
        if not es_vocal(letra):
            aux+=letra
        else:
            aux+=letra+"p"+letra
if __name__ == "__main__": 
  return aux