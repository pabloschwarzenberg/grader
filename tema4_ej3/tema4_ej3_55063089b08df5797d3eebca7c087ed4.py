def jerigonzo(string):
    for i in range(len(string)):
      if i=="a":
        r=string.replace(a,apa)
      elif i=="e":
        r=string.replace(e,epe)      
      elif i=="i":
        r=string.replace(i,ipi)
      elif i=="o":
        r=string.replace(o,opo) 
      elif i=="u":
        r=string.replace(u,upu)  
    return string

if __name__ == "__main__":
  string=str(input("Ingrese una palabra: "))
  print(string)
  
         