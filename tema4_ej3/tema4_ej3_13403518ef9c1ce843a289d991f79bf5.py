vocales ="aeiou"
def jerigonzo(string):
    palabra = []
    for i in string:
        if i in vocales:
            p = "p"
            palabra.append(i)
            palabra.append(p)
            palabra.append(i)
        elif i not in vocales:
            palabra.append(i)
    string=""
    for i in palabra:
        string+= i
        
    return string


if __name__ == "__main__":
    traducir = input("Qué palabra quieres traducir?")
    print (jerigonzo(traducir))
         

         