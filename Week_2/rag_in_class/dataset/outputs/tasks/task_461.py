def upper_ctr(str):
    upper_ctr = 0
    for char in str:
        if 'A' <= char <= 'Z':
            upper_ctr += 1
    return upper_ctr
