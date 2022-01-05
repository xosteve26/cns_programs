def encryption(plainText, keyword):
    cipherText = ''
    for i in range(0, len(plainText)):
        x = (ord(plainText[i])+ord(keyword[i])) % 26
        x += 65
        cipherText += chr(x)

    return cipherText


def decryption(cipherText, keyword):
    plainText = ''
    for i in range(0, len(cipherText)):
        x = (ord(cipherText[i])-ord(keyword[i])) % 26
        x += 65
        plainText += chr(x)

    return plainText


def main():
    plaintext = input("Enter plaintext: ").replace(" ", "").upper()
    keyword = input("Enter keyword: ").replace(" ", "").upper()
    if len(keyword) < len(plaintext):
        for i in range(0, len(plaintext) - len(keyword)):
            keyword += keyword[i]

    print(keyword)

    enc = encryption(plaintext, keyword)
    print(enc)

    dec = decryption(enc, keyword)
    print(dec)


if __name__ == '__main__':
    main()
