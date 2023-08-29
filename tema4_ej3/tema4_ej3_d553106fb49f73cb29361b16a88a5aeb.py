def jerigonzo(palabra):
    i = 0
    while i < len(palabra):
        print(i,palabra)
        if palabra[i] in ['a','e','i','o','u']:
            palabra = palabra[:i+1] + 'p' + palabra[i] + palabra[i+1:]
            i += 2   
        i+=1
    return palabra

if __name__ == "__main__":
    palabra = int(input("escriba una palabra: "))
    print(jerigonzo(palabra))