s = 'CodeSpeedy'
k = 4
enc = [[" " for i in range(len(s))] for j in range(k)]
for i in enc:
    print(i)

print("\n")


def row_check(row, flag):
    if(row == 0):
        flag = 0
    elif row == k-1:
        flag = 1
    if(flag == 0):
        row += 1
    else:
        row -= 1
    return row, flag


def encryption():
    row = 0
    flag = 0

    for i in range(len(s)):
        enc[row][i] = s[i]
        print(row, flag, s[i])
        row, flag = row_check(row, flag)

    for j in enc:
        print(j)
    return enc


def decryption(enc):
    pt = ''
    flag = 0
    row = 0
    for i in range(len(s)):
        pt += enc[row][i]
        row, flag = row_check(row, flag)

    return pt


def main():
    enc = encryption()
    for i in range(k):
        print("".join(enc[i]))

    dec = decryption(enc)
    print(dec)


if __name__ == "__main__":
    main()
