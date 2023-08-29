def buscarTodas(c,b):
    position = ""
    number= 0
    for indice in c:
        if indice == b:
            if position == "":
                number_str = str(number)
                position += number_str
                number += 1
            else:
                position += " "
                number_str = str(number)
                position += number_str
                number += 1
        else:
            number += 1
    return position

if __name__ == " __main__ ":
    pass