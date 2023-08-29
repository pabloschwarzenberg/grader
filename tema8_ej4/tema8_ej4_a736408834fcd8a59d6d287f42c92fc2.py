def rot13(word):
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            if char.islower():
                encrypted_word += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                encrypted_word += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            encrypted_word += char
    return encrypted_word