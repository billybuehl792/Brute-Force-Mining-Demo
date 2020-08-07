#!python3
# base_convert.py - convert from base 10 to base n

import string

def base10_to_n(ks, num=0):
    base = len(ks)
    result = ''

    while True:
        currentNum = num % base
        num = num // base
        result = ks[currentNum] + result
        if num == 0:
            break
    
    return result

def n_to_base10(ks, string):
    base10_val = 0
    multiplier = len(string) - 1

    for k in string:
        try:
            base10_val += (len(ks) ** multiplier) * ks.index(k)
            multiplier -= 1
        except ValueError:
            return 'Error: String characters not in keyspace'

    return base10_val

# bases
binary = '01'
abc = 'abcdef'
ternary = '123'
hexadecimal = '0123456789ABCDEF'
alphabet = string.ascii_letters

base_n = binary

for n in range(30):
    print(f'base10: {str(n)}, \
            base{len(base_n)}: {base10_to_n(base_n, n)}, \
            back to base10: {n_to_base10(base_n, base10_to_n(base_n, n))}')
