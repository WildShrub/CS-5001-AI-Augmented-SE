def number_of_substrings(s):
    length = len(s)
    return int(length * (length + 1) / 2)
