def palindromo(palabra):
    if len(palabra) == 1:
        return True
    else:
        l1 = list(palabra)
        l2 = list(palabra)
        l2.reverse()
        if l1[0] == l2[0]:
            l1.pop(0)
            l1.pop(-1)
            palabra = "".join(l1)
            return palindromo(palabra)
        else:
            return False
    

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           