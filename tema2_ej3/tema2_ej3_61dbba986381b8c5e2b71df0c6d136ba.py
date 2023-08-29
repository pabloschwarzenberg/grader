def numero_perfecto(a):
    Lista_1 = [1]
    for b in range(2, a + 1):
        if a % b == 0:
            Lista_1.append(b)
            if a in Lista_1:
                Lista_1.remove(a)
                if sum(Lista_1) == a:
                    return True
                else:
                    return False
if __name__ == "__main__":
  print(numero_perfecto(6))