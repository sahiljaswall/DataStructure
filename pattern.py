"""
1.

for x in range(5,0,-1):
    for y in range(1,x+1):
        print(y, end= " ")
    print(end="\n")"""
"""
row=5
for x in range(row):
    print(" "*(row-x-1), end="")
    print("*"*(2*(x)+1))"""

""""
3.

*********
 *******
  *****
   ***
    *
"""
"""
4.

row = 5
for x in range(row,0,-1):
    print(" "*(row-x), end="")
    print("*"*(2*(x)-1))

"""
"""
5.
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *

row=5
for x in range(row):
    print(" "*(row-x-1), end="")
    print("*"*(2*(x)+1))
for x in range(row,0,-1):
    print(" "*(row-x), end="")
    print("*"*(2*(x)-1))
"""
"""
6.
*
**
***
****
*****
*****
****
***
**
*
row=5
for x in range(row+1):
    print("*"*(x))
for x in range(row,0,-1):
    print("*"*x)"""
"""
7.

1
0 1
1 0 1
0 1 0 1
1 0 1 0 1
n=5
for x in range(0,n+1):
        for y in range(0,x):
            if (x+y)%2==0:
                print("0" ,end=" ")
            else:
                 print("1", end=" ")
        print(end="\n")"""

"""
8.

1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
row=5
count=1
for x in range(row+1):
    for y in range(0,x):
        print(count,end=" ")
        count+=1
    print(end="\n")"""
"""
9.
A
A B
A B C
A B C D
A B C D E
row=5
count=65
for x in range(row+1):
    for y in range(x):
        print(chr(count), end=" ")
        count+=1
    count=65
    print(end="\n")"""
"""
10.
A B C D E 
A B C D
A B C
A B
A
row=5
count=65
for x in range(row):
    for y in range(row,x,-1):
        print(chr(count), end=" ")
        count+=1
    count=65
    print(end="\n")"""
"""
11.
A
BB
CCC
DDDD
EEEEE
row=5
count=65
for x in range(row):
    for y in range(x+1):
        print(chr(count), end="")
    print(end="\n")
    count+=1
"""
"""
12.
   A
  ABA
 ABCBA
ABCDCBA
row=4 
for x in range(1,row+1):
    spaces=' '*(row-x)
    front = ''.join(chr(65+y) for y in range(x)) 
    back = front[-2::-1]
    print(spaces+front+back)
"""
"""
13.
E
D E
C D E
B C D E
A B C D E
row = 5
for x in range(row):
    letter = chr(65+row-x-1)
    line = ' '.join(chr(ord(letter)+y) for y in range(x+1) )
    print(line)"""
