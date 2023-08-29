def jerigonzo(string):
    result = ""
    for s in string:
        result += s
        if s.lower() == "a":
            result += "pa"
        if s.lower() == "e":
            result += "pe"
        if s.lower() == "i":
            result += "pi"
        if s.lower() == "o":
            result += "po"
        if s.lower() == "u":
            result += "pu"

    return result

if __name__ == "__main__":
    pass
        