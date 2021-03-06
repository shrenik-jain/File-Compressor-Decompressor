# File-Compressor-Decompressor


- [Introduction](#introduction)
- [Hufman Coding](#huffman-coding)
- [Linear Block Codes](#Linear-Block-Codes)
- [Decompression](#Decompression)
- [Usage](#Usage)


***
### Introduction
- A python administered project which uses Huffman Encoding Technique to compress a text file into a binary file.
- Utilizes Linear Block Codes to identify any errors committed while compression.
***

### Huffman Coding

- The thought process behind Huffman encoding is that a letter or a symbol which occurs frequently is represented by a shorter code, and the one that appears rarely is represented by a longer code. This leads to an efficient representation of characters that require less memory to be stored.

- To compress a sequence of characters, we need a table that gives us the sequences of bits used for each character. This table creates an encoding tree that uses the root/leaf path to create a bit sequence to encodes the characters. Using this we can create a list of all characters with the maximum bit length of the encoded characters and the number of occurrences.

- To construct an optimal tree, we use a greedy algorithm. Huffman encoding trees return the minimum length character encodings used in data compression. The nodes in the tree represent the frequency of a character’s occurrence. The root node represents the length of the string, and traversing the tree gives us the character-specific encodings. Once the tree is constructed, traversing the tree gives us the respective codes for each symbol.

<p align="center">
<img src="https://user-images.githubusercontent.com/50694291/102987833-f8d31400-4538-11eb-937d-8c271c3a9c9c.png" width="640px" height="480px"> </p>

***

### Linear Block Codes

- In coding theory, a linear code is an error-correcting code for which any linear combination of codewords is also a codeword. Linear codes are traditionally partitioned into block codes and convolutional codes, although turbo codes can be seen as a hybrid of these two types. Linear codes allow for more efficient encoding and decoding algorithms than other codes.

- Linear codes are used in forward error correction and are applied in methods for transmitting symbols (e.g., bits) on a communications channel so that, if errors occur in the communication, some errors can be corrected or detected by the recipient of a message block. The codewords in a linear block code are blocks of symbols that are encoded using more symbols than the original value to be sent.

- A linear code of length n transmits blocks containing n symbols. For example, the [7,4] Hamming code is a linear binary code which represents 4-bit messages using 7-bit codewords. Two distinct codewords differ in at least three bits. As a consequence, the error detecting ability is 2 bits per codeword while the error correcting ability is 1.

<p align="center">
<img src="https://user-images.githubusercontent.com/50694291/102988626-2ec4c800-453a-11eb-9cde-3b4a3a805e0e.png" width="640px" height="480px"> </p>

***

### Decompression

- For the final and easiest step, we use a hashmap data structure. 

- We loop through the binary file and keep adding the binary digits to an empty string curr_code until it matches with one of the codewords in the hashmap whose corresponding symbol added to string decode.

- As soon as we add the decoded character or symbol to the decode, the curr_code is again made empty and the same process is repeated from the next binary digit.
***

### Usage

- Run `decompress.py`

***
