def verification(Ka, Kb):
    if (Ka == Kb):
        return True
    else:
        return False


def calculation(alpha, XA, XB, q):
    # compute public keys
    YA = (alpha ** XA) % q
    YB = (alpha ** XB) % q
    # Public keys are shared between both parties and secret keys Ka,Kb are computed
    KA = (YB**XA) % q
    KB = (YA**XB) % q
    return KA, KB


def main():
    XA = int(input("Enter XA: "))
    XB = int(input("Enter XB: "))
    q = int(input("Enter A prime number: "))
    alpha = int(input("Enter a primitive root: "))
    Ka, Kb = calculation(alpha, XA, XB, q)
    verify = verification(Ka, Kb)

    if verify:
        print("Diffy Key Exchange Successful")
    else:
        print("Diffy Key Exchange Failed")


if __name__ == '__main__':
    main()
