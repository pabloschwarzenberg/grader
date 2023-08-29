def jerigonzo(string):
    t=""
    for i in(string):
      if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        t=t+i+"p"+i
      else:
        t=t+i
    return t
if __name__=="__main__":
    string=input("Ingrese su texto: ")
    print(jerigonzo(string))
    pass
         