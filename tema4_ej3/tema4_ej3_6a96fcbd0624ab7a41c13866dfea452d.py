vocales = {
    "a": "apa",
    "e": "epe",
    "i": "ipi",
    "o": "opo",
    "u": "upu",
}


def jerigonzo(string):
    str_lst = list(string)
    for i, char in enumerate(str_lst):
        char = char.lower()
        print(str_lst)
        if char in vocales.keys():
            str_lst[i] = vocales[char]
    return "".join(str_lst)


if __name__ == "__main__":
  print(jerigonzo())