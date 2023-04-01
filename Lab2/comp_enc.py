import math, time


def decBin(rest, x):
    binary = str(bin(rest)[2:])
    return binary.rjust(x, '0')


def getFromFile():
    with open('do_kompresji.txt', 'r', encoding='utf-8') as file:
        data = ''.join(file.read())
    return data


def encrypt():
    asciiTab = [[col + row - 256 if col + row > 255 else col + row
                 for col in range(256)] for row in range(256)]

    encTab = []
    index = 0

    for char in res:
        keyChar = ord(key[index])
        encTab.append(asciiTab[keyChar][char])
        index = (index + 1) % len(key)

    return encTab


if __name__ == '__main__':
    key = input('Key: ')
    if len(key) == 0:
        print('No key')
        exit()

    dataBin = ''
    data = getFromFile()
    dataDict = sorted(list(set(data)))

    X = len(dataDict)
    N = math.ceil(math.log2(X))
    R = (8 - (3 + N * len(data))%8)%8

    print(f'X = {X}\nN = {N}\nR = {R}')
    print(f'File lenght before compression: {len(data)}')
    startTime = time.time()

    res = bytearray()
    res.append(X)

    for j in dataDict:
        res.append(ord(j))
        
    dataBin = decBin(R, 3)
    binSecond = ''

    for char in data:
        binSecond += decBin(dataDict.index(char), N) 
        
    binSecond += str(1) * R
    dataBin += binSecond

    for i in range(0, len(dataBin), 8):
        swToChar = chr(int(dataBin[i:(i+8)], 2))
        res.append(ord(swToChar))

    encTab = encrypt()

    with open('skompresowany_e.txt', 'wb') as comp:
        comp.write(bytes(encTab))

    endTime = time.time()
    print(f'File lenght after compression: {len(encTab)}')
    print(f'Elapsed time {endTime - startTime}')