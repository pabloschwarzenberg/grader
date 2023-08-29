def rot13(palabra):

   

    abc="abcdefghijklmnñopqrstuvwxyz"



    largo = len(palabra)

    k=13

    i = 0

    cifrad = ""

    newposicion = 0

    for c in palabra:

        if c in abc:

           
            i = (abc.index(c)+k)%(len(abc))
            if i == len(abc) or (abc.index(c)+k) == 26: i = 0
            if i > k + 1 and i < len(abc)-1: i = i + 1
         
           
            cifrad += abc[i]


        else:

            cifrad+=c



    return cifrad