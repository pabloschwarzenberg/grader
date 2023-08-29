def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    contador=0
    jeri=[]
    while contador<len(string):
      contador2=0
      while contador2<len(vocales):
        if string[contador]==vocales[contador2]:
          jeri.append(vocales[contador2])
          jeri.append("p")
        contador2+=1
      jeri.append(string[contador])
      contador+=1
    jeri="".join(jeri)
    return jeri

if __name__ == "__main__":
    pass
         