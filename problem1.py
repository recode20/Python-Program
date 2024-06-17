""" Given a maximum of four digits to the base 17(10-> A, 11-> B, 12-> C, 16-> G) as
 input, output its decimal value.
 Input:
 23GF"""


import math
import string

def Sweet_Seventeen():
    j={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16}
    k=0
    s=0
    
    for i in m:
        if i in string.digits:
            k=int(i)

            s+=k*(int(math.pow(17,m.index(i))))
            
        elif i in j:
            
            s+=j[i]*int((math.pow(17,m.index(i))))
            
    print("Total:",s)

n=""
lst=[]
n=input("Enter a value \n (BUT 'PLEASE DO NOT ENTER 2 SIMILAR DIGITS'):")
lst=list(n)
print(lst)
m=[]
m=lst[::-1]
print(m)
Sweet_Seventeen()