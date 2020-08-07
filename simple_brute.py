#!python3
# simple_brute.py - iterate over keyspaces

import hashlib
from string import ascii_letters, digits


class Brute:

    def __init__(self, ks, f, maxLen):
        self.ks = ks
        self.f = f
        self.maxLen = maxLen
        self.l = 1

    def brutef(self, s='', r=1):
        # recursively iterate through each permutation of a keyspace to len(n)
        if r == 1:
            while self.l <= self.maxLen:
                for k in self.ks:
                    permutation = s + k
                    if r < self.l:
                        self.brutef(permutation, r+1)
                    else:
                        self.f(permutation)
                self.l += 1
        else:
            for k in self.ks:
                permutation = s + k
                if r < self.l:
                    self.brutef(permutation, r+1)
                else:
                    self.f(permutation)

    @staticmethod
    def n_to_base10(ks, permutation):
        # convert string permutation(composed of keys from ks) to base10
        base10_val = -1
        multiplier = len(permutation) - 1

        for k in permutation:
            try:
                base10_val += (len(ks) ** multiplier) * (ks.index(k) + 1)
                multiplier -= 1
            except ValueError:
                return 'Error: String characters not in keyspace'

        return base10_val

    @staticmethod
    def base10_to_n(ks, num=0):
        # convert integer to base n string
        base = len(ks)
        result = ''

        while True:
            currentNum = num % base
            num = (num // base) - 1
            result = ks[currentNum] + result
            if num < 0:
                break
        
        return result


# specify action with each permutation
def find_hash(permutation):
    global hashlist

    h = hashlib.md5(permutation.encode()).hexdigest()

    if h in hashlist:
        print(f'HASH MATCH! Permutation: {permutation}, Digest: {str(h)}')

if __name__ == '__main__':
    # keyspaces
    ks1 = 'abc'
    ks2 = 'xyz123'
    ks3 = ascii_letters + digits

    # maximum permutation length
    max_length = 5

    # retrieve hash list
    with open('hashes.txt', 'r') as f:
        hashlist = [line.strip('\n') for line in f]

    # brute force key space
    b = Brute(ks3, find_hash, max_length)
    b.brutef()

    # convert between base10 and baseN
    print(f'Base10: 52, BaseN: {Brute.base10_to_n(ks3, 52)}')
    print(f'BaseN: aa, Base10: {Brute.n_to_base10(ks3, "aa")}')
