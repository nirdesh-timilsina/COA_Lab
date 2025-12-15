# Objective : to design N- bit adder for unsigned integer binary numbers
#first input 
print ("Enter n bit binary strings: ")
A = input("A: ")
if any (el not in '01' for el in A):
   raise ValueError("Only enter binary number.")

B = input("B:")
if any (el not in '01' for el in B):
    raise ValueError ("Only enter binary number.")

if len(A) != len(B):
    raise ValueError("both inputs must be of same bit length.")
length = len(A)
def fullAdder( a,  b,  c):
    s = a^b^c
    Carry = a*b + (a^b)*c
    return s,Carry
s,c = 0,0
sum_ans =""
for i in range (length -1 ,-1,-1):
    a,b = int(A[i]),int(B[i])
    s,c = fullAdder(a,b,c)
    sum_ans = str(s)+sum_ans

print (f"A: {A},B: {B},sum :{sum_ans}, carry : {c}")
