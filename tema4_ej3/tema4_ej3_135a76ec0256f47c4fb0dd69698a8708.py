def jerigonzo(string):
    v= string
    v= list(string)
    for a,b in enumerate(v):
        if b=="a"or b=="e"or b=="i"or b=="o"or b=="u":
            v[a]+= ("p" + v[a])
    string = "".join(v)
    return string


if __name__ == "__main__":
    pass
         