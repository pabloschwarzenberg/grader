def rot13(word):
    encrypted_word = ''
    for char in word:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - 97 + 13) % 26 + 97)
            else:
                encrypted_char = chr((ord(char) - 65 + 13) % 26 + 65)
        else:
            encrypted_char = char
        encrypted_word += encrypted_char
    return encrypted_word

           