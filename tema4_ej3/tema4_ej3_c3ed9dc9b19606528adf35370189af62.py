def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    translate=list(string)
    i=0
    for j in range(len(translate)):
      if (translate[i] in vocales) is True:
        x=vocales.index(translate[i])
        translate.insert(i+1,"p")
        translate.insert(i+2,vocales[x])
        i+=3
      else:
        i+=1
    string="".join(translate)
    return string

if __name__ == "__main__":
    pass
         