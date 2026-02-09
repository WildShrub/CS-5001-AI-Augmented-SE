def find_Max_Len_Even(str):
    n = len(str)
    i = 0
    currlen = 0
    maxlen = 0
    st = -1

    while i < n:
        if str[i] == ' ':
            if currlen % 2 == 0 and currlen > maxlen:
                maxlen = currlen
                st = i - currlen
            currlen = 0
        else:
            currlen += 1
        i += 1

    if currlen % 2 == 0 and currlen > maxlen:
        maxlen = currlen
        st = i - currlen

    return str[st:st + maxlen] if st != -1 else "-1"
