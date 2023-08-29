def jerigonzo(string):
    indice=""
    for letra in string:
      if "a" in letra:
        indice+="apa"
      elif "e" in letra:
        indice+="epe"
      elif "i" in letra:
        indice+="ipi"
      elif "o" in letra:
        indice+="opo"
      elif "u" in letra:
        indice+="upu"
      else:
        indice+=letra
      
    return indice

if __name__ == "__main__":
    pass
         