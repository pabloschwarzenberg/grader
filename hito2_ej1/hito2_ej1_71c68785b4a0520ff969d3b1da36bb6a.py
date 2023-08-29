def align_sequences(s1, s2):
    aligned_s2 = ""
    i = 0
    for char in s1:
        if char == s2[i]:
            aligned_s2 += s2[i]
            i += 1
        else:
            aligned_s2 += "_"
    
    if i < len(s2):
        aligned_s2 += s2[i:]
    
    return aligned_s2


# Ejemplo de uso
s1 = input("Ingresa la primera secuencia de ADN: ")
s2 = input("Ingresa la segunda secuencia de ADN: ")

aligned_s2 = align_sequences(s1, s2)

print(aligned_s2)
      