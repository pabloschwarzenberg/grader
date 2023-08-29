def palindromo(palabra):
    if len(palabra)<2: return True
    elif palabra[0]==palabra[-1]: return palindromo(palabra[1:-1])
    else: return False