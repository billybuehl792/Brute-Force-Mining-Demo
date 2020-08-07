#!python3
# mineDemo.py - how finding SMALL hashes works... except slow and pathetic with python
# https://www.blockchain.com/explorer

import hashlib
import sys
import time
from bitcoin import privtopub, pubtoaddr


class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    ENDC = '\033[0m'


def keyCreation(phrase):
    priv = hashlib.sha256(str(phrase).encode()).hexdigest()
    pub = privtopub(priv)
    addr = pubtoaddr(pub)

    return(priv, pub, addr)

def getTarget(leadingZeros):
    target = hex(16**(63-leadingZeros))
    # target = '0x' + hex(16**(63-leadingZeros))[2:].zfill(64)
    print(f'Target: {Color.YELLOW}{target}{Color.ENDC}\n')

    return(target)

def findHash(target):
    value = 0
    t1 = time.time()
    while True:
        h = hashlib.sha256(str(value).encode()).hexdigest()
        if (value%100000) == 0:
            print(f'hash: {str(h)}\nvalue: {str(value)}\n')
        value+=1

        if int(h, 16) < int(target, 16):
            print(f'{Color.GREEN}Success!!{Color.ENDC}')
            print(f'time elapsed: {str(time.time() - t1)}\nvalue hashed: {str(value)}')
            break


if __name__ == '__main__':
    try:
        leadingZeros = int(sys.argv[1])
    except:
        leadingZeros = int(input('Leading 0s in target: '))

    target = getTarget(leadingZeros)
    findHash(target)
