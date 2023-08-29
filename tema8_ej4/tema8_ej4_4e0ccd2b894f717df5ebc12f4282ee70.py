def rot13(palabra):
    a=("abcdefghijklmnopqrstuvwxyzabcdefghijklm")
    c=""
    for b in palabra:
        c=c+a[a.find(b)+13]
    return c

if __name__=="__main__":
    print(rot13(input("ingrese palabra: ")))
           