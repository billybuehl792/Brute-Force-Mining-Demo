#!python3
# simple_brute.py - iterate over keyspaces

import hashlib
import string


class Brute:

    def __init__(self, ks, n, maxLen):
        self.ks = ks
        self.n = n
        self.maxLen = maxLen
        self.l = 1
        self.counter = 0

    def action(self, permutation):
        # specify action for each nth permutation
        if self.counter % n == 0:   
            h = hashlib.md5(permutation.encode()).hexdigest()
            print(f'Value: {permutation}, Hash: {str(h)}')

        self.counter += 1

    def brutef(self, s='', r=1):
        # recursively iterate through each permutation of a keyspace to len(n)
        if r == 1:
            while self.l <= self.maxLen:
                for k in self.ks:
                    permutation = s + k
                    if r < self.l:
                        self.brutef(permutation, r+1)
                    else:
                        self.action(permutation)
                self.l += 1
        else:
            for k in self.ks:
                permutation = s + k
                if r < self.l:
                    self.brutef(permutation, r+1)
                else:
                    self.action(permutation)

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


if __name__ == '__main__':
    # keyspaces
    ks1 = 'abc'
    ks2 = 'xyz123'
    ks3 = string.ascii_letters

    # maximum permutation length
    max_length = 6

    # action every n
    n = 1

    # brute force key space
    b = Brute(ks2, n, max_length)
    b.brutef()

    # convert 
    print(f'Base10: 52, BaseN: {Brute.base10_to_n(ks3, 52)}')
    print(f'BaseN: aa, Base10: {Brute.n_to_base10(ks3, "aa")}')
