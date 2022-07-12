# МАТРИЦЫ
import random

KEYS_INDS = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 6, 5, 4, 3, 2, 1]

S = [

    [4, 10, 9, 2, 13, 8, 0, 14, 6, 11, 1, 12, 7, 15, 5, 3],
    [14, 11, 4, 12, 6, 13, 15, 10, 2, 3, 8, 1, 0, 7, 5, 9],
    [5, 8, 1, 13, 10, 3, 4, 2, 14, 15, 12, 7, 6, 0, 9, 11],
    [7, 13, 10, 1, 0, 8, 9, 15, 14, 4, 6, 12, 11, 2, 5, 3],
    [6, 12, 7, 1, 5, 15, 13, 8, 4, 10, 9, 14, 0, 3, 11, 2],
    [4, 11, 10, 0, 7, 2, 1, 13, 3, 6, 8, 5, 12, 15, 14],
    [13, 11, 4, 1, 3, 15, 5, 9, 0, 10, 14, 7, 6, 8, 2, 12],
    [1, 15, 13, 0, 5, 7, 10, 4, 9, 2, 3, 14, 6, 11, 8, 12],

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


def toHex(s):
    return (hex(int(s, 2))[2::]).upper()


def genRandKey(length):
    binKeyR = [random.randint(0, 1) for i in range(length)]
    binKey = ''
    for item in binKeyR:
        binKey += str(item)
    return binKey


# Общие функции


# ОСНОВНЫЕ АЛГОРИТМЫ

def L(s):
    return s[0:len(s) // 2]


def R(s):
    return s[len(s) // 2::]


def leftShift(s, cnt):
    for i in range(cnt):
        s = s[1:len(s)] + s[0]
    return s


def genSubKeys(binKey):
    #print(binKey)
    subKeys = [binKey[i*32:i*32+32:] for i in range(8)]
    rezSubKeys = []
    for num in KEYS_INDS:
        rezSubKeys.append(subKeys[num - 1])

    return rezSubKeys


def plusModulo2(a, b):
    ans = ''
    for i in range(len(a)):
        ans += str(int(a[i]) ^ int(b[i]))
    return ans


def F(R, K):
    vsp = (int(R, 2) + int(K, 2)) % 32
    vsp = bi(vsp).zfill(32)
    bin4Numbers = []
    for i in range(8):
        bin4Numbers.append(vsp[i * 4:i * 4 + 4])

    binRez = ''
    for i, bin4num in enumerate(bin4Numbers):
        decnum = int(bin4num, 2)
        binRez += bi(S[i][decnum]).zfill(4)

    shiftedBinRez = leftShift(binRez, 11)
    return shiftedBinRez


def blockGOST(block, key):
    subKeys = genSubKeys(key)
    # print(subKeys)
    data = block
    lastL = L(data)
    lastR = R(data)
    for i in range(32):
        l = lastR
        r = plusModulo2(lastL, F(lastR, subKeys[i]))
        lastL = l
        lastR = r
    data = lastR + lastL

    return data


def blockUN_GOST(block, key):
    subKeys = genSubKeys(key)
    data = block
    lastL = L(data)
    lastR = R(data)
    for i in range(32):
        l = lastR
        r = plusModulo2(lastL, F(lastR, subKeys[32 - i - 1]))
        lastL = l
        lastR = r
    data = lastR + lastL
    return data


def GOST(bins, key):
    cnt = 0
    while len(bins) % 64 != 0:
        bins += '0'
        cnt += 1
    bins += bi(cnt).zfill(64)
    blocks = binToBlocks(bins)
    ans = ''
    for block in blocks:
        ans += blockGOST(block, key)
    return ans


def UN_GOST(bins, key):
    blocks = binToBlocks(bins)

    ans = ''
    for block in blocks:
        ans += blockUN_GOST(block, key)

    cnt = int(binToBlocks(ans)[-1], 2)
    ans = ans[:-64:]
    if cnt > 0:
        ans = ans[:-cnt:]

    return ans



encrypt = GOST
decrypt = UN_GOST


#binKey = '0001001100110100010101110111100110011011101111001101111111110001000100110011010001010111011110011001101110111100110111111111000100010011001101000101011101111001100110111011110011011111111100010001001100110100010101110111100110011011101111001101111111110001'
#binKey = genRandKey(256)
binKey = '1110010101100110010011100110101000111110100101100000011000100101100110110011001011111111111100011011010100110111000001010010110011111001100101110101011000111000110111010000010011111110111000111011001001011101010111011011101001001011011101001111011011111000'
print(binKey)

filePath = 'C:\\Users\\Максим\\Desktop\\123.txt'

f = open(filePath, 'rb')
inp = f.read()
f.close()
# print(inp)


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






