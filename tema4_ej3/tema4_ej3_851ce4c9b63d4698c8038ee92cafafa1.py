def jerigonzo(string):
    nuevo = ""
    vowals = ["a","e","i","o","u"]
    for i in str(string):
        if i in vowals:
            nuevo += str(i)+"p"+str(i)
        else:
            nuevo += str(i)
    return nuevo
if __name__ == "__main__":
    pass
         