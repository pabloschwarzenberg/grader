def levenshtein(palabra1,palabra2):
    palabra1_list= []
    palabra2_list = []
    palabra1_list[:0]=palabra1
    palabra2_list[:0]=palabra2

    counter = 0

    diff = abs(len(palabra1)-len(palabra2))

    if len(palabra1) > len(palabra2):
        for i in range(diff):
            palabra2_list.append(" ")
    else:
        for i in range(diff):
            palabra1_list.append(" ")

    for i in range(len(palabra1_list)):
        for j in range(len(palabra2_list)):
            if palabra1_list[i] == palabra2_list[j]:
                palabra1_list[i] = "-"
                palabra2_list[j] = "-"
                break

    counter1 = 0
    counter2 = 0

    for x in range(len(palabra1_list)):
        if not (palabra1_list[x] == " " or palabra1_list[x] == "-"):
            counter1 = counter1 + 1

    for z in range(len(palabra2_list)):
        if not (palabra2_list[z] == " " or palabra2_list[z] == "-"):
            counter2 = counter2 + 1

    resultado = ''

    if counter1 == 1 and counter2 == 1:
        resultado = resultado + '1S'
    elif (counter1 == 1 and counter2 == 0) or (counter1 == 0 and counter2 == 1):
        resultado = resultado + 'IB'
    elif (counter1 == 0 and counter2 == 0):
        resultado = resultado + '0D'
    else:
        resultado = resultado + '+1'

    print(counter1, counter2)
    print(resultado)

    return resultado