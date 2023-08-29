def jerigonzo(palabra):    
    tradu=""
    for i in palabra:
        if i in "AEIOUaeiou":
            tradu+=i
            tradu+="p"
        tradu+=i
    return tradu