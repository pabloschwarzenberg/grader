def jerigonzo(p):
     mover = ""
     for l in p:
         if l in "aeiou":
             mover += l
             #agregar p después de cada vocal
             mover += "p"
         mover += l
     return mover

if __name__ == "__main__":
    pass
         