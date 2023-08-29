def rot13(word):
    result = ''
    for char in word:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
            result += encrypted_char
        else:
            result += char
    return result
           