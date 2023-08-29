def rot13(word):
    result = ""
    for char in word:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result
           