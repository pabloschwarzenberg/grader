s=str(input())
def secuencia(string):
    i=0
    while(i<len(string)):
      if(string[i]!="A")or(string[i]!="C")or(string[i]!="G")or(string[i]!="T"):
        return "La secuencia es incorrecta"
      elif(string[i]!="a")or(string[i]!="c")or(string[i]!="g")or(string[i]!="t"):
        return "La secuencia es incorrecta"
      else:
        return "La secuencia es correcta"
       
print(secuencia(s))
