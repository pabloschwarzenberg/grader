def palindromo(p1):
    p2 = invertir_palabra(p1)
    if p1 == p2:
        return True
    return False
def invertir_palabra(p1):
    p2 = ''
    if p1 == '' or len(p1) == 1:
        p2 = p1 + p2
        return p2
    return invertir_palabra(p1[len(p1)-1]) + invertir_palabra(p1[:len(p1)-1])

if __name__=="__main__":
    print(palindromo("oso"))
    print(palindromo("dinosaurio"))
           