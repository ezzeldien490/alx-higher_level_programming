#!/usr/bin/python3

def remove_char_at(str, n):
    i = len(str)
    cp_str = list(str)

    if n >= i or n < 0:
        for r in range(len(str)):
            cp_str[r] = str[r]

    else:
        for r in range(n):
            cp_str[r] = str[r]

        for r in range(n, len(str)):
            cp_str[n] = str[n + 1]

    return ''.join(cp_str)
