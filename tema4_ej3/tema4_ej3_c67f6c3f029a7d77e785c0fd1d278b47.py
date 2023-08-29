def jerigonzo(string):
    r=string.replace('a','apa').replace('e','epe').replace('i','ipi').replace('o','opo').replace('u','upu').replace('A','Apa').replace('E','Epe').replace('I','Ipi').replace('O','Opo').replace('U','Upu')
    return r
    
if __name__ == "__main__":
    R=input()
    print(jerigonzo(R))   
         