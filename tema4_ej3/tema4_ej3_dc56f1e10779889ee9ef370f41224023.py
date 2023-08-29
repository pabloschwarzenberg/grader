vocal = "AÁEÉIÍOÓUÚaáeéiíoóuú"
def jerigonzo(string):
    j = ""
    
    for i in string:
        if i not in vocal:
            j = j+i
        if i in vocal:
            j = j+i+"p"+i
        else:
            continue        
    return j
if __name__ == "__main__":
    pass
         