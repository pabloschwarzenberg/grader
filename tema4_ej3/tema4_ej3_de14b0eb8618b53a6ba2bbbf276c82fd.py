def jerigonzo(string):
    palabra=[]
    for letra in string:
      palabra.append(letra)
      if letra=="a":
        palabra.append("p")
        palabra.append("a")
      elif letra=="e":
        palabra.append("p")
        palabra.append("e")
      elif letra=="i":
        palabra.append("p")
        palabra.append("i")
      elif letra=="o":
        palabra.append("p")
        palabra.append("o")
      elif letra=="u":
        palabra.append("p")
        palabra.append("u")
    return "".join(palabra)     