def create_n_tokens(str, delim, n):
    parts = str.split(delim)

    if n > 0 :
        return delim.join(parts[0: n])
    else :
        l = len(parts)
        start = l + n
        if start < 0: start = 0

        return delim.join(parts[start: l])