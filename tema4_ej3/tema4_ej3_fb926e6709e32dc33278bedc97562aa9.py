def jerigonzo(string):
    palabranueva = ""
    for i in string:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            palabranueva += i+"p"+i

        else:
            palabranueva += i

    return palabranueva
