import string
old_chars = "ACGT"
replace_chars = "TGCA"
tab = string.maketrans(old_chars,replace_chars)
print "AAAACCCGGT".translate(tab)[::-1]