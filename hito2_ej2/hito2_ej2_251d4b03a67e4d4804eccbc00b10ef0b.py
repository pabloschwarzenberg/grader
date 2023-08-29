def validez(cadena: str) -> str:
    for caracter in cadena.casefold():
        if caracter not in ['a', 'c', 't', 'g','b']:
            return 'Secuencia incorrecta'
    return 'Secuencia correcta'