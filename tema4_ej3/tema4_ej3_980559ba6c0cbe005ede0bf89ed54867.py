def jerigonzo(string):
    l = list(string)
    vo = ['a','e','i','o','u']
    for letra in l:
        if letra in vo:
            l.insert(l.index(letra),'p')
            l.insert(l.index(letra)+1,letra)
            
    h = string
    return h

if __name__ == "__main__":
    pass
         