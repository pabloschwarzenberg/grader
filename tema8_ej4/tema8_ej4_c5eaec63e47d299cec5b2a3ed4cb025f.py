def rot13(word):
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            encrypted_word += encrypted_char
        else:
            encrypted_word += char
    return encrypted_word
