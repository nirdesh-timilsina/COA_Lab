# Objective : to design n bit (4-bit) adder for unsigned integer binary numbers
#first input 
print ("Enter 4 bit binary strings: ")
A = input("A: ")
if len(A)!=4 or any (el not in '01' for el in A):
   raise ValueError("Only enter binary number of length 4.")
B = input("B:")
if len(B)!= 4 or any (el not in '01' for el in B):
    raise ValueError ("Only enter binary number of length 4.")
def fullAdder( a,  b,  c):
    s = a^b^c
    Carry = a*b + (a^b)*c
    return s,Carry
s,c = 0,0
sum_ans =""
for i in range (3,-1,-1):
    a,b = int(A[i]),int(B[i])
    s,c = fullAdder(a,b,c)
    sum_ans = str(s)+sum_ans

print (f"A: {A},B: {B},sum :{sum_ans}, carry : {c}")

