def jerigonzo(string):
    out_str = ""
    for char in string:
        if char in ["a","e","i","o","u"]:
            out_str += char + "p" + char
        else:
            out_str += char
    return out_str


if __name__ == "__main__":
    pass
         