def jerigonzo(string):
    z = [str(x) for x in string]
    print(len(z))
    for x,n in enumerate(z):
        if n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u':
            z.insert(x+1, 'p')
    for x, n in enumerate(z):
        if n == 'p' and z[x-1] != ' ':
            z.insert(x+1 , z[x-1])
    Pal = ''.join([str(y) for y in z])
    return(Pal)