def jerigonzo(string):
    n = (len(string))
    i = 0
    palabra = []
    String = []
    for x in string:
        palabra.append(x)
        String.append(x)
    while(n >= i):
        if n == i:
            break
        k = String.index(String[i])
        if String[k] == 'a':
            String.pop(k)
            String.insert(k, 'A')
            String.insert(k, 'p')
            String.insert(k, 'A')
            n = n + 2
        elif String[k] == 'e':
            String.pop(k)
            String.insert(k, 'E')
            String.insert(k, 'p')
            String.insert(k, 'E')
            n = n + 2
        
        elif String[k] == 'i':
            String.pop(k)
            String.insert(k, 'I')
            String.insert(k, 'p')
            String.insert(k, 'I')
            n = n + 2
        
        elif String[k] == 'o':
            String.pop(k)
            String.insert(k, 'O')
            String.insert(k, 'p')
            String.insert(k, 'O')
            n = n + 2
       
        elif String[k] == 'u':
            String.pop(k)
            String.insert(k, 'U')
            String.insert(k, 'p')
            String.insert(k, 'U')
            n = n + 2
        i = i + 1
        
    string = ''
    for j in String:
        if (65 <= ord(j) <= 90):
            r = ord(j) + 32
            j = chr(r)
        string = string + j
    return string

if __name__ == "__main__":
    string = str(input('Ingresa texto:' ))
    print(jerigonzo(string))