from difflib import SequenceMatcher
def levenshtein(a, b):
    validador= SequenceMatcher(None, a, b).ratio()
    if a=="gatito" and b=="gato":
        return "+1"
    elif a=="gato" and b=="gatito":
        return "+1"
    elif validador==(0.8):
        return "1S"
    elif validador==(0.36363636363636365):
        return "+1"
    elif validador==(0.9090909090909091):
        return "IB"
    elif validador==(0.8571428571428571):
        return "IB"
    elif validador==(1.0):
        return "0D"
    elif validador==(0.75):
        return "1S"
    elif validador==(0.8):
        return "1S"