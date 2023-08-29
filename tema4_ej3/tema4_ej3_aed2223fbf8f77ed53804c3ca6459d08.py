def jeringozo(string):
    string=""
    for letra in string:
        if not es_vocal(letra):
            string+=letra
        else:
            string+=letra+"p"+letra
    return string
if __name__ == "__main__":
    string=input()