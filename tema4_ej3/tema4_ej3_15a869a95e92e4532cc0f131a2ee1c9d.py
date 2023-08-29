def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
def jerigonzo(string):
  word = ""
  vowels = ["a","A","e","E", "i", "I", "o", "O", "u", "U"]
  for letrita in string:
    if letrita in vowels:
      word += letrita
      word += "p"
    word += letrita

  return word         