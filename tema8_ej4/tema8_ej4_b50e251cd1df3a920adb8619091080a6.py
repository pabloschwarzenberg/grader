def rot13(palabra):

    abecedario = "abcdefghijklmnopqrstuvwxyz"

    nueva = ""

    for i in palabra:

        print(i)

        if i in abecedario:



            if abecedario.index(i) < 13:



                nueva += abecedario[abecedario.index(i) + 13]

            else:

                nueva += abecedario[abecedario.index(i) - 13]

    return nueva