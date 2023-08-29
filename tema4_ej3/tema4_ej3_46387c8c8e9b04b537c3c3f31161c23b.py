def jerigonzo(string):
    listota = []
    for word in string:
        for let in word:
            if let in "aeiouAEIOU":
                let = let + "p" + let
            listota.append(let)
    listota = "".join(listota)
    return listota