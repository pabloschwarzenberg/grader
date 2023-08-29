def jerigonzo(string):
    convertido = []
    for palab in string:
        for let in palab:
            if let in "aeiouAEIOU":
                let = let + "p"+ let
            convertido.append(let)
    convertido = "".join(convertido)
    return convertido