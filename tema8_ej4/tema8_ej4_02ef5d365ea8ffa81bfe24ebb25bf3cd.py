def rot13(palabra):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    list1 = list(palabra)

    for num in range(len(list1)):
        index1 = letras.index(list1[num])
        if index1 <= 12:
            list1[num] = letras[index1+13]
        else:
            list1[num] = letras[index1-13]

    return ''.join(list1)