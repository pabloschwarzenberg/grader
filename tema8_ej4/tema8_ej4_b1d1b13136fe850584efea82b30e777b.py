def rot13(palabra):
    ad=[]
    abc={'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m'}
    for i in range (len(palabra)):
        p=palabra[i]
        ad.append(abc[p])
    print(ad)
    t="" .join(ad)
    return t