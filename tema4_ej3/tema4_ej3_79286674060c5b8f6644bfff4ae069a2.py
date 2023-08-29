def jerigonzo(string):
    vocales=['a','e','i','o','u']
    convertida=""
    for i in string:
        if i in vocales:
            convertida+=i+"p"+i
        else:
            convertida+=i
    string=convertida

    return string

if __name__ == "__main__":
    print(jerigonzo(input("Ingrese palabra a jerigonzoar: ")))
         