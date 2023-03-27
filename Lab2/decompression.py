import math

def decypher(compressedText):
    key = input('Key: ')

    if len(key) == 0:
        print('No key')
        exit()
        
    asciiTable = [[col + row - 256 if col + row > 255 else col + row
                   for col in range(256)] for row in range(256)]

    index = 0
    decypherText = []

    for char in compressedText:
        keyChar = ord(key[index])
        decypherText.append(asciiTable[keyChar].index(char))
        index = (index+1) % len(key)
        
    return decypherText
        


if __name__ == '__main__':
    with open('skompresowany.txt', 'rb') as file:
        compressedText = [i for i in file.read()]
    
    try: 
        compressedText_D = decypher(compressedText)
        
        dataDict = compressedText_D[0]
        
        dictionary = [chr(compressedText_D[i]) for i in range(1, dataDict + 1)]
        
        list_to_decompress = [bin(compressedText[i])[2:].zfill(8) 
                            for i in range(dataDict + 1, len(compressedText_D))]
        
        bin_text = ''.join(list_to_decompress)
        
        to_decompress = bin_text[3:len(bin_text)-(int(bin_text[:3], 2))]
        
        N = math.ceil(math.log2(dataDict))
        
        decompressed = [dictionary[int(to_decompress[i:(i+N)], 2)]
                        for i in range(0, len(to_decompress), N)]
        
        # print(decompressed)

        with open('zdekompresowany2.txt', 'w', encoding='utf-8') as file2:
            file2.write(''.join(decompressed))
        


    except(ValueError, IndexError):
        print('error')