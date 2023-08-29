def validar(s):
    a=s.lower()
    l="actg"
    for i in a:
        if not(i in l):
            return("secuencia incorrecta")
    return("secuencia correcta")
s=input()
print(validar(s))