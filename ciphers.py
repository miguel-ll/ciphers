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

#text = "hello world"
#s = 3
#message = caesar_enc(text,s)
#print(message)

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

#    message = "HELLO"
#    result = encrypt(message.upper())
#    print (result)
#    result = decrypt(result)
#    print (result)

#with open('declaration.txt') as f:
#    lines = [line for line in f]

#txt = ["we","shall","dissolve","and","kill"]

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
#print(book_dec(book_enc(txt,lines),lines))
