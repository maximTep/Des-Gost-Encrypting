import math
import random
# МАТРИЦЫ

IP = [

    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
    56, 48, 40, 32, 24, 16, 8, 0,
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6

]

inverseIP = [

    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25,
    32, 0, 40, 8, 48, 16, 56, 24,

]

PC1 = [

    56, 48, 40, 32, 24, 16, 8,
    0, 57, 49, 41, 33, 25, 17,
    9, 1, 58, 50, 42, 34, 26,
    18, 10, 2, 59, 51, 43, 35,
    62, 54, 46, 38, 30, 22, 14,
    6, 61, 53, 45, 37, 29, 21,
    13, 5, 60, 52, 44, 36, 28,
    20, 12, 4, 27, 19, 11, 3

]

PC2 = [

    13, 16, 10, 23, 0, 4,
    2, 27, 14, 5, 20, 9,
    22, 18, 11, 3, 25, 7,
    15, 6, 26, 19, 12, 1,
    40, 51, 30, 36, 46, 54,
    29, 39, 50, 44, 32, 47,
    43, 48, 38, 55, 33, 52,
    45, 41, 49, 35, 28, 31

]

EXP = [

    31, 0, 1, 2, 3, 4,
    3, 4, 5, 6, 7, 8,
    7, 8, 9, 10, 11, 12,
    11, 12, 13, 14, 15, 16,
    15, 16, 17, 18, 19, 20,
    19, 20, 21, 22, 23, 24,
    23, 24, 25, 26, 27, 28,
    27, 28, 29, 30, 31, 0

]

S = [

    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]

]

P = [

    15, 6, 19, 20, 28, 11, 27, 16,
    0, 14, 22, 25, 4, 17, 30, 9,
    1, 7, 23, 13, 31, 26, 2, 8,
    18, 12, 29, 5, 21, 10, 3, 24

]

ROTATES = [

    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1

]

# МАТРИЦЫ


# Общие функции



def bi(num):
    return bin(num)[2:len(bin(num))]


def strToBin(s):
    rez = ''
    for el in s:
        rez += bi(ord(el)).zfill(8)
    return rez


def fileBinToStrBin(s):
    rez = ''
    for el in s:
        rez += bi(el).zfill(8)
    return rez


def binToBlocks(bin):
    rez = []

    for i in range(len(bin) // 64):
        rez.append(bin[64*i:64*i+64:])

    return rez


def hex2bin(he):
    return bin(int(he, 16))[2:].zfill(8)


def bin2text(s):
    return "".join([chr(int(s[i:i+8], 2)) for i in range(0, len(s), 8)])

# Общие функции


# ОСНОВНЫЕ АЛГОРИТМЫ

def permutate(matr, block):
    rez = ''
    for i in range(len(matr)):
        rez += (block[matr[i]])
    return str(rez)


def L(s):
    return s[0:len(s) // 2]


def R(s):
    return s[len(s) // 2::]


def genSubKey(key):
    return permutate(PC1, key)


def leftShift(s, cnt):
    for i in range(cnt):
        s = s[1:len(s)] + s[0]
    return s


def genShiftedSubKeys(binSubKey):
    subKeys = [[L(binSubKey), R(binSubKey)]]
    for i in range(16):
        subKeys.append([leftShift(subKeys[-1][0], ROTATES[i]), leftShift(subKeys[-1][1], ROTATES[i])])
    subKeys1 = [i[0] + i[1] for i in subKeys]
    #print(subKeys1)
    subKeys1.pop(0)
    return subKeys1


def binKeyToShiftedPermutatedKeys(binKey):
    subKey = genSubKey(binKey)
    subKeys = genShiftedSubKeys(subKey)
    permutatedSubKeys = [permutate(PC2, k) for k in subKeys]
    #print(permutatedSubKeys)
    return permutatedSubKeys


def plusModulo2(a, b):
    ans = ''
    for i in range(len(a)):
        ans += str(int(a[i]) ^ int(b[i]))
    return ans


def E(bit32Block):
    rez = ''
    #print(len(bit32Block))
    for i in range(len(EXP)):
        rez += (bit32Block[EXP[i]])
    return str(rez)


def F(R, K):
    vsp = plusModulo2(K, E(R))
    B = []
    for i in range(8):
        B.append(vsp[i * 6:i * 6 + 6])
    #print(B)
    rez = ''
    for i, b in enumerate(B):
        row = int(b[0] + b[-1], 2)
        col = int(b[1] + b[2] + b[3] + b[4], 2)
        rez += bi(S[i][row][col]).zfill(4)
    rez = permutate(P, rez)
    return rez


def blockDES(block, key):
    subKeys = binKeyToShiftedPermutatedKeys(key)
    #print(subKeys)
    data = permutate(IP, block)
    lastL = L(data)
    lastR = R(data)
    for i in range(16):
        l = lastR
        r = plusModulo2(lastL, F(lastR, subKeys[i]))
        lastL = l
        lastR = r
    data = lastR + lastL
    data = permutate(inverseIP, data)

    return data


def blockUN_DES(block, key):
    subKeys = binKeyToShiftedPermutatedKeys(key)
    data = permutate(IP, block)
    lastL = L(data)
    lastR = R(data)
    for i in range(16):
        l = lastR
        r = plusModulo2(lastL, F(lastR, subKeys[16 - i - 1]))
        lastL = l
        lastR = r
    data = lastR + lastL
    data = permutate(inverseIP, data)
    return data


def toHex(s):
    return (hex(int(s, 2))[2::]).upper()


def DES(bins, key):
    cnt = 0
    while len(bins) % 64 != 0:
        bins += '0'
        cnt += 1
    bins += bi(cnt).zfill(64)
    blocks = binToBlocks(bins)
    ans = ''
    for block in blocks:
        ans += blockDES(block, key)
    return ans


def UN_DES(bins, key):
    blocks = binToBlocks(bins)

    ans = ''
    for block in blocks:
        ans += blockUN_DES(block, key)

    cnt = int(binToBlocks(ans)[-1], 2)
    ans = ans[:-64:]
    if cnt > 0:
        ans = ans[:-cnt:]

    return ans


def HEX_DES(bins, key):
    return toHex(DES(bins, key))


def HEX_UN_DES(bins, key):
    s = int(bins, 16)
    bins = hex2bin(bins)
    return UN_DES(bins, key)


encrypt = DES
decrypt = UN_DES


binKey = '0001001100110100010101110111100110011011101111001101111111110001'
# data = '11010100101010100'


filePath = 'C:\\Users\\Максим\\Desktop\\123.docx'

f = open(filePath, 'rb')
inp = f.read()
f.close()
print(inp)


if __name__ == '__main__':
    mode = int(input('1 - зашифровать\n2 - расшифровать\n'))
    if mode == 1:
        f = open(filePath, 'wb')
        inp = inp.decode()
        inp = strToBin(inp)
        crypted = encrypt(inp, binKey)
        # print(crypted)
        # print(crypted.encode())
        f.write(bin2text(crypted).encode())
    elif mode == 2:
        f = open(filePath, 'wb')
        inp = inp.decode()
        inp = strToBin(inp)
        decrypted = decrypt(inp, binKey)
        # print('decrypted = ', decrypted)
        # print('decrypted.encode = ', decrypted.encode())
        f.write(bin2text(decrypted).encode())



f.close()






