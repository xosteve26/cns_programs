
def transform(matrix,s,col_limit):
    row=0
    col=0
    j = 0
    while j<len(s):
        if (col == col_limit):
            col=0
            row+=1
        matrix[row][col] = s[j]
        j+=1
       
        col+=1
    return matrix
        
def encryption(matrix,row_limit,col_limit):
    c=0
    r=0
    cipher=''
    l=0
    while l <row_limit*col_limit:
        cipher+=matrix[r][c]
        r+=1
        if r == row_limit:
            r=0
            c+=1
        l+=1
    return cipher

def decryption(matrix):

    decypher=''
    for i in matrix:
        decypher+=''.join(i)

    return decypher

def main():
    s = 'helloworld'
    row_limit=3
    col_limit=4
    matrix = [[" " for i in range(col_limit)]for j in range(row_limit)]
    result=transform(matrix,s,col_limit)
    print(result)
    enc=encryption(result,row_limit,col_limit)
    dec=decryption(matrix)
    print(enc.replace(' ',''))
    print(dec)

    
if __name__ == '__main__':
    main()