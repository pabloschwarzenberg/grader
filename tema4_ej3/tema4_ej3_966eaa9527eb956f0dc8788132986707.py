def jerigonzo(string):
    vocal = ['a','e','i','o','u']
    n = list(string)
    jer = ''

    for i in range (0,len(n)):
        s = n[i]
        if s in vocal:
            jer += (s+'p' + s)
        else:
            jer += s

    return jer
if __name__ == "__main__":
    a = input('Ingrese una palabra: ')
    print(jerigonzo(a))
         