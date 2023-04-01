import math, time


if __name__ == '__main__':
    startTime = time.time()
    with open('skompresowany.txt', 'rb') as compressed:
        data = [i for i in compressed.read()]
    
    uniqueSymbols = data[0]
    dataDict = [chr(data[i]) for i in range(1, uniqueSymbols + 1)]
    
    toDecomp_L = [bin(data[i])[2:].zfill(8) for i in range(uniqueSymbols + 1, len(data))]
    binText = ''.join(toDecomp_L)

    rest = int(binText[:3], 2)
    toDecomp = binText[3:(len(binText) - rest)]

    N = math.ceil(math.log2(uniqueSymbols))
    decompressed = [dataDict[int(toDecomp[i:(i + N)], 2)] for i in range(0, len(toDecomp), N)]

    with open('zdekompresowany.txt', 'w', encoding='utf-8') as decomp:
        decomp.write(''.join(decompressed))

    endTime = time.time()
    print(f'Elapsed time {endTime - startTime}')
