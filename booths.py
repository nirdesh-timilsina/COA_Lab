# Booth's Multiplication

A = input("Enter multiplicand: ")
if any(el not in '01' for el in A):
    raise ValueError("Must enter binary string!")

B = input("Enter multiplier: ")
if any(el not in '01' for el in B):
    raise ValueError("Must enter binary string!")

n = max(len(A), len(B))

# sign extend to same length
A = A.zfill(n)
B = B.zfill(n)

def full_adder(a, b, c):
    aint = int(a)
    bint = int(b)
    cint = int(c)
    s = aint ^ bint ^ cint
    carry = aint*bint + (aint ^ bint)*cint
    return str(s), str(carry)

def addBinary(A, B):
    c = '0'
    result = ''
    for a, b in zip(reversed(A), reversed(B)):
        s, c = full_adder(a, b, c)
        result = s + result
    return result

def twos_complement(X):
    # 1's complement
    inv = ''.join('1' if b == '0' else '0' for b in X)
    # +1
    one = '0'*(len(X)-1) + '1'
    return addBinary(inv, one)

def arithmetic_right_shift(A, Q, Q_1):
    combined = A + Q + Q_1
    msb = combined[0]          # sign bit
    combined = msb + combined[:-1]
    return combined[:n], combined[n:2*n], combined[-1]

def booths_multiplication(M, Q):
    A = '0' * n
    Q_1 = '0'

    for _ in range(n):
        if Q[-1] == '1' and Q_1 == '0':
            # A = A - M
            A = addBinary(A, twos_complement(M))
        elif Q[-1] == '0' and Q_1 == '1':
            # A = A + M
            A = addBinary(A, M)

        A, Q, Q_1 = arithmetic_right_shift(A, Q, Q_1)

    return A + Q

print("Result:", booths_multiplication(A, B))
