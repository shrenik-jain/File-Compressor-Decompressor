from Huffman import *
from lbc import *

curr_code = ""
decode = ""

for i in range(len(real_s)):
    curr_code += real_s[i]

    if(curr_code in rmap):
        character = rmap[curr_code]
        decode += character
        curr_code = ""

print("\nThe Decoded Text is:")
print(decode)