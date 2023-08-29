def jerigonzo(string):
    p =list(string)
    pf = ''
    vocal = ['a','e','i','o','u']
    for i in range (0,len(p)):
        l = p[i]
        if l in vocal:
            pf += l+'p'+l
        else:
            pf += l
    return pf

if __name__ == "__main__":
    palabra= input("ingrese palabra:")
    print(jerigonzo(palabra))
         