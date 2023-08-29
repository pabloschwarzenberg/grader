def jerigonzo(string):
    s_lista=list(string)
    i=0
    n_string=""
    while i < len(s_lista):
      if s_lista[i]=="a":
        n_string+="apa"
        i+=1
      elif s_lista[i]=="e":
        n_string+="epe"
        i+=1
      elif s_lista[i]=="i":
        n_string+="ipi"
        i+=1
      elif s_lista[i]=="o":
        n_string+="opo"
        i+=1  
      elif s_lista[i]=="u":
        n_string+="opu"
        i+=1
      else:
        n_string+=s_lista[i]
        i+=1
    return n_string

if __name__ == "__main__":
    pass
         