def jerigonzo(palabro):
    lst = []
    tiene_vocales = False
    while palabro != '':
        tiene_vocales = False
        for i in palabro:
            if i in 'aeiou':
                tiene_vocales = True
                break
        if not tiene_vocales:
            lst.append(palabro)
            break
        for i in range(len(palabro)):
            if palabro[i] in 'aeiou':
                lst.append(palabro[:i+1])
                palabro = palabro[i+1:]
                break
    output = ''
    aux = ''
    if not tiene_vocales:
        aux = lst.pop(-1)
    for i in lst:
        i += 'p' + i[-1]
        output += i
    output += aux
    return output

if __name__ == "__main__":
    pass
         