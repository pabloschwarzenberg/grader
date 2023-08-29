def jerigonzo(string):
    vocal=["a","e","i","o","u"]
    hola=""
    lista=[]
    for i in string:
      lista.append(i)
      if i in vocal:
        lista.append("p"+i)
    for j in lista:
      hola+=j
    return hola

if __name__ == "__main__":
    pass
         