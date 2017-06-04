import heapq
import sys
import string
from HuffmanCoding import HuffmanCoding
from collections import defaultdict

BUFFER_SIZE = 100000
BUFFER_SIZE1= []


def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

filename='chunk1.txt'
f = open(filename,'rb')
data = f.read(BUFFER_SIZE)
frequency = defaultdict(int)
for symbol in data:
    frequency[symbol] += 1

huff = encode(frequency)
print "Symbol".ljust(10) + "Frequency".ljust(10) + "Codeword"
for p in huff:
    print p[0].ljust(10) + str(frequency[p[0]]).ljust(10) + p[1]
    BUFFER_SIZE1.append(p[1])
print BUFFER_SIZE1
my_lst_str = ''.join(map(str, BUFFER_SIZE1))
print(my_lst_str)
print len(my_lst_str)
path = "/Users/basilmimi/Desktop/chunk1.txt"
h = HuffmanCoding(path)
output_path = h.compress()
