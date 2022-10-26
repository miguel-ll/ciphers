def rot13(text):
    s = 13
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
             result += chr((ord(char) + s-65) % 26 + 65)
        elif (char.islower()):
             result += chr((ord(char) + s -97) % 26 + 97)
        else:
         	result += char;
    return result

def rot47(message):
    key = 47
    encryp_text = ""

    for i in range(len(message)):
        temp = ord(message[i]) + key
        if ord(message[i]) == 32:
            encryp_text += " "
        elif temp > 126:
            temp -= 94
            encryp_text += chr(temp)
        else:
            encryp_text += chr(temp)
    return encryp_text

def atbash(text):
      N = ord('z') + ord('a')
      ans=''
      return ans.join([chr(N - ord(s)) for s in text])

# right shift is done instead of left shift
def caesar_enc(text,s,right=True):
    if not right:
    	s *= -1
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
             result += chr((ord(char) + s-65) % 26 + 65)
        elif (char.islower()):
             result += chr((ord(char) + s -97) % 26 + 97)
        else:
         	result += char;
    return result

def caesar_dec(message):
    for i in range(1,27):
	    print(f"Key {i}:",caesar_enc(message, i))

def morse_enc(message):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '
    return cipher

def morse_dec(message):
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
    message += ' '
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2 :
                decipher += ' '
            else:
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
    return decipher

def find_index(tt,lines):
    c1 = 0; c2 = 0
    for words in lines:
        wds = words.split()
        c1 += 1
        c2 = 0
        for ws in wds:
            c2 += 1
            if ws == tt:
                return [c1,c2]

def find_word(tt,lines):
    a = tt[0]-1
    b = tt[1]-1
    wds = lines[a].split()
    return wds[b]

def book_enc(tt,lines):
    li = []
    for i in range(len(tt)):
        li.append(find_index(tt[i],lines))
    return li

def book_dec(tt,lines):
    li = []
    for z in range(len(tt)):
        li.append(find_word(tt[z],lines))
    return li

def encryptRailfence(text, key):
    # create the matrix to cipher
    rail = [['\n' for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):
        # check the direction of flow
        # reverse the direction if we've just
        # filled the top or bottom rail
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        # fill the corresponding alphabet
        rail[row][col] = text[i]
        col += 1
        # find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher using the rail matrix
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return("" . join(result))

def decryptRailfence(cipher, key):
    # create the matrix to cipher
    rail = [['\n' for i in range(len(cipher))] for j in range(key)]
    dir_down = None
    row, col = 0, 0
    # mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        # place the marker
        rail[row][col] = '*'
        col += 1
        # find the next row using direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    # now we can construct the fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
    # now read the matrix in
    # zig-zag manner to construct
    # the resultant text
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        # place the marker
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
        # find the next row using
        # direction flag
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

#x = encryptRailfence("defend the east wall", 3)
#print(decryptRailfence(x, 3))
