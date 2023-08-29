def jerigonzo(string):
    arr_text = list(string)
    for index in range(0, len(arr_text)):
        letra = arr_text[index]
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            arr_text[index] = letra + 'p' + letra
    return "".join(arr_text)
    
if __name__ == "__main__":
    pass
         