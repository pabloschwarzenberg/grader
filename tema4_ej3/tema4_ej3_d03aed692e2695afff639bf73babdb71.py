def jerigonzo(string):
  palabra_a = string.replace("a", "apa")
  palabra_ae = palabra_a.replace("e", "epe")
  palabra_aei = palabra_ae.replace("i", "ipi")
  palabra_aeio = palabra_aei.replace("o", "opo")
  palabra_aeiou = palabra_aeio.replace("u", "upu")
  return palabra_aeiou