def jerigonzo(string):
    x=1
    v=['a','e','i','o','u']
    string=list(string)
    for i in string:
        if i in v:
            string.insert(x,'p'+ i)
        x=x+1
    string=''.join(string)
    return string
    print(string)

if __name__ == "__main__":
    pass
jerigonzo('hola')
print(jerigonzo('hola'))