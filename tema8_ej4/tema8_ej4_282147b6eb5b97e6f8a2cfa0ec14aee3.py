def rot13(palabra):
    newPal=''
    l1="abcdefghijklm"
    l2="nopqrstuvwxyz"
    for i in range(len(palabra)):
        if l1.__contains__(palabra[i]):
            print("esta en l1")
            newPal=newPal+l2[l1.index(palabra[i])]
        else:
            print("esta en l2")
            newPal = newPal + l1[l2.index(palabra[i])]
    return newPal
           