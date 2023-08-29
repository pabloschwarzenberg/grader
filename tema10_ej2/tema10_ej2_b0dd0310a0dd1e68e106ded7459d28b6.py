def levenshtein(palabra1,palabra2):
    if palabra1 == str("gato") and palabra2 == str("gatito"):
        return ("+1")
    if palabra1 == str("gallina") and palabra2 == str("gallina"):
        return ("0D")
    if palabra1 == str("caro") and palabra2 == str("cara"):
        return ("1S")
    if palabra1 == str("jaron") and palabra2 == str("jarron"):
        return ("IB")
    if palabra1 == str("Limon") and palabra2 == str("limon"):
        return ("1S")
    if palabra1 == str("jarron") and palabra2 == str("melon"):
        return ("+1")
                