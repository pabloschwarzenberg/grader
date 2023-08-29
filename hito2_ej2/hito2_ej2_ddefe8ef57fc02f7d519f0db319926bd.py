def validar_secuencia(secuencia):
    sec = secuencia.lower()
    a = len(sec)
    secl = list(sec)
    cuenta = 0
    for i in ("a","c","t","g"):
        cuenta += secl.count(i)
    if a == cuenta:
        return "secuencia correcta"
    else:
        return "secuencia incorrecta"
print(validar_secuencia(input()))
