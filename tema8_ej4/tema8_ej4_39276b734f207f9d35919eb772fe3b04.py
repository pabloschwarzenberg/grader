def rot13(result):
    resu = ""
    res = 'UANDRESBELLO'
   # res = input("Ingrese la palabra para encriptar: ")

    res.lower()
    var = "abcdefghijklmnopqrstuvwxyz"
    fun = var[13:]+var[:13]
    char = lambda c: fun[var.find(c)] if var.find(c)>-1 else c

    return resu.join( char(c) for c in result )

print(rot13('result'))
           