def jerigonzo(x):
    b=list(x)
    for i in range(0,(len(x)+7)):
        if b[i]=="a":
            if i == len(b)+1:
                b.append("pa")
            else:
               b.insert(i+1,"pa")
        elif b[i]=="e":
            if i == len(b)+1:
                b.append("pa")
            else:
               b.insert(i+1,"pe")
        elif b[i]=="i":
            if i == len(b)+1:
                b.append("pa")
            else:
                b.insert(i+1,"pi")
        elif b[i]=="o":
            if i == len(b)+1:
                b.append("pa")
            else:
                b.insert(i+1,"po")
        elif b[i]=="u":
            if i == len(b)+1:
                b.append("pa")
            else:
              b.insert(i+1,"pu")
        else:
            continue
        a="".join(b)
    return a
