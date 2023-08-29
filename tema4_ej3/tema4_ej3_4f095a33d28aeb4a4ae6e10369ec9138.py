def jerigonzo(string):
    listastr=list(string)
    i=0
    while i<len(listastr):
      if listastr[i]=="a":
        listastr.insert((i+1),"pa")
      elif listastr[i]=="e":
        listastr.insert((i+1),"pe") 
      elif listastr[i]=="i":
        listastr.insert((i+1),"pi")
      elif listastr[i]=="o":
        listastr.insert((i+1),"po")
      elif listastr[i]=="u":
        listastr.insert((i+1),"pu")   
      i=i+1  
    
    string="".join(listastr)
    return string

if __name__ == "__main__":
    string=input("ingrese palabra")
         