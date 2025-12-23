# Multiplication

A = input ("Enter first number: ")
if any (el not in '01' for el in A):
    raise ValueError("Must enter binary string!")
B = input ("Enter second number: ")
if any (el not in '01' for el in B):
    raise ValueError("Must enter binary string!")
# if len(A) != len(B):
#     raise ValueError("Must enter both string of same bit length.")

def full_adder( a,b,c):
    aint = int(a)
    bint= int(b)
    cint= int(c)
    s= aint^bint^cint
    carry = aint*bint + (aint^bint)*cint
    s = str(s)
    carry = str(carry)
    return s , carry
def addBinary(A,B):
    c_init = '0'
    sum_total= ''
    for a, b in zip(reversed(A), reversed(B)):
        sum_step, c_init = full_adder(a, b, c_init)
        sum_total = sum_step + sum_total
    
    return sum_total, c_init
def bin_multiplication(A,B):
    n = len(A)
    bit_padding = '0'*n
    A_mul = bit_padding + A
    #B_mul = bit_padding + B
    product = '0' * 2*n #register to store the intermediate value
    for b in reversed(B):
        if b =='1':
            product = addBinary(A_mul,product)[0]
        A_mul = A_mul[1:] + '0'
    return product

print ("Result: ",bin_multiplication(A,B))
