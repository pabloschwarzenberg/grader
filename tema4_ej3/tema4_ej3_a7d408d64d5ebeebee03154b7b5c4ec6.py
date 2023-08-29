def jerigonzo(string):
    D=string.replace('a','apa').replace('e','epe').replace('i','ipi').replace('o','opo').replace('u','upu').replace('A','Apa').replace('E','Epe').replace('I','Ipi').replace('O','Opo').replace('U','Upu').replace('á','ápa').replace('é','épe').replace('í','ípi').replace('ó','ópo').replace('ú','úpu')
    return D
    
if __name__ == "__main__":
    d=input()
    print(jerigonzo(d))    