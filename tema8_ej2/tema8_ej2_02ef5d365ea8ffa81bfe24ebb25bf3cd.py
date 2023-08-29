def buscarTodas(a,b):

    string1_list = []
    for index1 in range(len(a)):
        if a[index1] == b:
            string1_list.append(str(index1))
            string1_list.append(' ')


    string1 = ''.join(string1_list)
    string1 = string1.strip()
    return string1