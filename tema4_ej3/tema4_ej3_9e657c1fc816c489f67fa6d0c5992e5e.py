def jerigonzo(string):
    v = list('aeiou')

    for c in string:
        if c in v:
            string = string.replace(c, str(c+'p'+c))
            v.remove(c)
    
    return string
    
if __name__ == "__main__":
    
    jerigonzo('Hola buenos dias')
         