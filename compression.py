import os
import huffmanstat as hs
import zivlempel as zl

# Lorem Ipsum 5 paragraphs
fichier = 'loremipsum.txt'

with open(fichier, 'r') as f:
  data = f.read()

tailleFicihier = os.stat(fichier).st_size
tailleFichierBits = 8 * tailleFicihier

def pourcentageReduction(compr, fichier):
    decimal = compr / fichier
    return 100 - (100 * decimal)

print("Lorem Ipsum size = ", tailleFichierBits)

print("--------HUFFMAN STATIQUE---------")
# Compressed Huffman
comprHS = hs.comprimer(data)[0]
# print(comprHS)
print("New size = ", len(comprHS))
print("Percentage of old file = ", pourcentageReduction(len(comprHS), tailleFichierBits))

# Decompressed Huffman
decomprHS = hs.decoder(hs.comprimer(data)[0],hs.comprimer(data)[1])
# print(decomprHS)

#Correct?
print("Huffman statique correcte?")
print(decomprHS == data)

print("--------ZIV-LEMPEL---------")
#Compressed Ziv-Lempel
comprZL = zl.comprimer(data)
# print(comprZL)
print("New size = ", 8 * len(comprZL))
print("Percentage of old file = ", pourcentageReduction(8 * len(comprZL), tailleFichierBits))

# Decompressed Ziv-Lempel
decomprZL = zl.decomprimer(zl.comprimer(data))
# print(decomprZL)

#Correct?
print("Ziv Lempel correcte?")
print(decomprZL == data)