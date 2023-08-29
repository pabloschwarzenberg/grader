def jerigonzo(palabra):
    palabralista=list(palabra)
    palabramod=palabralista.copy()
    desdea = 0
    desdee = 0
    desdei = 0
    desdeo = 0
    desdeu = 0
    for x in palabralista:
        if x=="a":
            palabramod.insert(palabramod.index(x,desdea)+1,"pa")
            desdea=palabramod.index(x,desdea)+1
        elif x=="e":
            palabramod.insert(palabramod.index(x, desdee) + 1, "pe")
            desdee =  palabramod.index(x, desdee) + 1
        elif x=="i":
            palabramod.insert(palabramod.index(x, desdei) + 1, "pi")
            desdei =  palabramod.index(x, desdei) + 1
        elif x=="o":
            palabramod.insert(palabramod.index(x, desdeo) + 1, "po")
            desdeo =  palabramod.index(x, desdeo) + 1
        elif x=="u":
            palabramod.insert(palabramod.index(x, desdeu) + 1, "pu")
            desdeu =  palabramod.index(x, desdeu) + 1
        else:
            pass
    
    palabrafinal="".join(palabramod)
    return palabrafinal
if __name__ == "__main__":
    pass
         