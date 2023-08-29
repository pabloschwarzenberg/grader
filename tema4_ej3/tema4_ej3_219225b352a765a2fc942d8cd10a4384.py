def jerigonzo(string):
    VOCAL=["a", "e", "i", "o", "u"]
    copy=""
    for x in string:
        copy += x
        if x in VOCAL:
            copy += "p"+x
    string=copy
    return string

if __name__ == "__main__":
    pass
         