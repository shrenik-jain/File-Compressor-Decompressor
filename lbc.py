from Huffman import *

rows , cols = (30 , 30)
n , k = 7 , 4

C = [0 for _ in range(30)]

# print("Enter the Generator Matrix")
G = [[1,0,0,0,0,1,1],[0,1,0,0,1,1,0],[0,0,1,0,1,0,1],[0,0,0,1,1,1,1]]

print("The Generator Matrix is :\n",*G , "\n")

for mess in range(0 , len(s) , 4):

    M = list(map(int , real_s[mess:mess+4]))
    # M = list(map(int , input("Enter The Message Bits\n").split()))

    par = [[0 for i in range(cols)] for j in range(rows)]

    # Parity Matrix
    for i in range(k):
            for j in range(n-k):
                    par[i][j] = G[i][j+k]

    # Message Bits
    print("\nThe message bits are:\n" , *M)

    # Parity Bits
    print("\nThe Parity Bits :")
    for i in range(n-k):
            C[i] = 0
            for j in range(k):
                    C[i]=(C[i] + M[j] * par[j][i])%2
            print("C",i+1, "=" , C[i])

    # Codeword
    print("\nCode Word For Given Messege Bit:")
    for i in range(k):
            print(M[i] , sep='' , end='')

    for j in range(n - k):
            print(C[j] , sep='' , end='')

    print()