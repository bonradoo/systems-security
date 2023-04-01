import math, time


def decrypt(data):
    key = input('Key: ')
    if len(key) == 0:
        print('No key')
        exit()

    asciiTab = [[col + row - 256 if col + row > 255 else col + row
                 for col in range(256)] for row in range(256)]

    decTab = []
    index = 0

    for char in data:
        keyChar = ord(key[index])
        decTab.append(asciiTab[keyChar].index(char))
        index = (index + 1) % len(key)
    return decTab


if __name__ == '__main__':
    startTime = time.time()
    with open('skompresowany_e.txt', 'rb') as compressed:
        data_e = [i for i in compressed.read()]
    
    data = decrypt(data_e)
    uniqueSymbols = data[0]
    dataDict = [chr(data[i]) for i in range(1, uniqueSymbols + 1)]
    toDecomp_L = [bin(data[i])[2:].zfill(8) for i in range(uniqueSymbols + 1, len(data))]

    binText = ''.join(toDecomp_L)
    rest = int(binText[:3], 2)
    toDecomp = binText[3:(len(binText) - rest)]

    N = math.ceil(math.log2(uniqueSymbols))
    decompressed = [dataDict[int(toDecomp[i:(i + N)], 2)] for i in range(0, len(toDecomp), N)]

    with open('zdekompresowany_e.txt', 'w', encoding='utf-8') as decomp:
        decomp.write(''.join(decompressed))

    endTime = time.time()
    print(f'Elapsed time {endTime - startTime}')
