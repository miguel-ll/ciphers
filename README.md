# ciphers

**ciphers** is a library designed to implement methods used in cryptanalysis.

# Essential functions and usage

**ciphers.py:**

- `rot13(arg)` - Encrypt/Decrypt a text and returns using the rot13 cipher.
- `rot47(arg)` - Encrypt/Decrypt a text and returns using the rot47 cipher. 
- `atbash(arg)` - Encrypt/Decrypt a text and returns using the atbash cipher. 
- `caesar_enc(text,s,right)` - Encrypt a text, shifting it by a factor *s*, depending on the boolean value of right (by default, right=True), and returns, using the caesar cipher.
- `caesar_dec(arg)` - Prints all possible encryption factors of the caesar cipher (i.e, tries to decrypt the text and print).
- `morse_enc(arg)` - Converts a text to morse code and returns.
- `morse_dec(arg)` - Decrypts a text in morse and returns.
- `book_enc(tt,lines)` - Encrypt a text *tt* according to the argument *lines* retrieved from a text file and returns, using the book cipher. 
- `book_enc(tt,lines)` - Decrypt a text *tt* after a book cipher, according to the argument *lines* retrieved from a text file and returns. 

**fplot.py:** 

- `letters_dist(txt)` - Plots a distribuition based on the frequency of letters used in the text.
