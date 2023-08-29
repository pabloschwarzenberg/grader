def jerigonzo(mainString):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    separated = []
    for word in mainString:
        for character in word:
            if character in vowels:
                character += ("p"+ character)
            separated.append(character)
    separated = "".join(separated)
    return separated