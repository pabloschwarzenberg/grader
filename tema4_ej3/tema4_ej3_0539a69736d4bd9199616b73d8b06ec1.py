def jerigonzo(string):
    palabra=""
    pato="aeiouAEIOU"
    for i in string:
        if i in pato:
            palabra+=i
            palabra+="p"
        palabra+=i
    return palabra
if __name__ == "__main__":
    pass
         