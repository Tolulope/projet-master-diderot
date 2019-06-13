from heapq import heappush, heappop, heapify
from collections import Counter

def encoder(donnes):
    symbfreq = Counter(donnes)
    heap = [[wt, [sym, ""]] for sym, wt in symbfreq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    charcodes = sorted(heappop(heap)[1:], key=lambda p: (len(p[1]), p))
    return charcodes


def comprimer(donnes):
    huff = encoder(donnes)
    donnescodees = ""
    for c in donnes:
        for p in huff:
            if c == p[0]:
                donnescodees += str(p[1])
    return donnescodees, huff

def isCode(codepot, huff):
    for sublist in huff:
        if sublist[1] == codepot:
            return sublist[0]

def decoder(donnescodees, huff):
    codeacharcher = ""
    donneesdecodees = ""
    for n in donnescodees:
        codeacharcher += n
        if isCode(codeacharcher, huff):
            donneesdecodees += isCode(codeacharcher, huff)
            codeacharcher = ""
    return donneesdecodees

# print(decoder(comprimer("abracadabra")[0], comprimer("abracadabra")[1]))
