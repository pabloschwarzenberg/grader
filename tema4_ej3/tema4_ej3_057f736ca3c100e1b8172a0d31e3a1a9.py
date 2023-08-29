def jerigonzo(string):
    lista=["a","e","i","o","u"]
    palabra=""
    i=0
    for x in string:
        if x in lista:
           palabra=palabra+x+"p"+x
        else:
           palabra=palabra+string[i]
        i=i+1
    return palabra
    
      