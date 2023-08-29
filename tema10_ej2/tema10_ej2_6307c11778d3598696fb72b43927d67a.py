from difflib import ndiff


def levenshtein(str1, str2, ):
    counter = {"+": 0, "-": 0}
    for edit_code, *_ in ndiff(str1, str2):
        if edit_code == " ":
            yield max(counter.values())
            counter = {"+": 0, "-": 0}
        else:
            counter[edit_code] += 1
    yield max(counter.values())


