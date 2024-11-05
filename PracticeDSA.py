
#1. Reverse a Number
"""
n=int(input("Enter Number you want reverse :"))
rev =0
while(n>0):
    last_num = n%10
    rev = (rev*10)+last_num    
    n//=10
print(rev)"""


#2. Count Digits
"""
n=int(input("Enter Number you want to count :"))
cnt =0
while(n>0):
    cnt+=1
    n//=10
print(cnt)    
"""

#3. Check Palindrome 121 -> rev -> 121
"""
n = int(input("Write a number you want to check :"))
orignal = n
rev = 0
while (n>0):
    last_num = n%10
    rev = (rev*10)+last_num
    n//=10
if rev == orignal:
    print("Number is Palindrome")
else: 
    print("Number is not Palindrome")
"""

#4. GCD Or HCF


#5. Armstrong Number
"""
n = int(input("Enter Number to check its Armstrong or not : "))
sum =0
orignal = n
while(n>0):
    last_num = n%10
    sum =(last_num**3)+sum
    n//=10
if sum == orignal:
    print(str(orignal)+" is Armstrong Number")
else:
    print(str(orignal)+" is not Armstrong Number")"""

#6. Find Divisors of a Number

"""
n=int(input("Enter Number to findout Divisors : "))
for x in range(1,n+1):
    if n%x==0:
        print(x ,end=" ")"""
"""
f_list=[]
n=int(input("Enter Number to findout Divisors : "))
for x in range(1,int(n**0.5)):
    if n%x==0:
        f_list.append(x)
        f_list.append(int(n/x))
print(sorted(f_list))"""

#7. Check for Prime Numbers'
"""
n=int(input("Enter Number to findout its Prime or not : "))
cnt=0
for x in range(2,int(n/2)):
    if n%x==0:
        cnt+=1
if cnt>0:
    print(str(n)+" is not Prime Number")
else:
    print(str(n)+" is Prime Number")"""

#8. GCD or HCF
"""
n = int(input("Enter First integers: "))
m = int(input("Enter Second integers: "))
for x in range(min(n,m), 1,-1):
    if n%x==0 and m%x==0:
        print(str(x)+" is GCD")
        break""" 
         
#9 Recursion : Print name 5 times
"""
n = int(input("How many time : "))
def printNames(i,n):
    if i>n:
        return
    print("Sahil Jaswal", end=" ")
    printNames(i+1,n)
printNames(1,n)
"""

#10 Recursion : Print linearly from 1 to N
"""
def printNumbers(n):
    if n<1:
        return
    printNumbers(n-1)
    print(n, end=" ")
n = int(input("How many time : "))
printNumbers(n)
"""

#10 Recursion : Print linearly from N to 1
"""
def printRevNumbers(i,n):
    if i>n:
        return
    printRevNumbers(i+1,n)
    print(i, end=" ")
n = int(input("How many time : "))
printRevNumbers(1,n)
"""

#11. Recursion : Sum of first N numbers
"""
def printSum(sum,i,n):
    if i>n:
        print(sum)
        return
    sum=sum+i
    printSum(sum,i+1,n)
n = int(input("Find the sum until 1 to : "))
printSum(0,1,n)

"""
"""
def printSum(n):
    if n==0:
        return 0
    return(n+printSum(n-1))
print(printSum(3))"""

#12. Recursion : Factorial
"""
def factorial(n):
    if n==0:
        return 1
    return(n*factorial(n-1))
print(factorial(5))
"""
#13. Recursion : Reverse array 
"""def f(i,arr, n):
    if i>=n/2:
        return 
    arr[i],arr[n]=arr[n],arr[i]
    f(i+1,arr,n-1)

arr=[1,4,2,8,5,3,21]
f(0,arr,len(arr)-1)
print(arr)

"""

#14. Recursion :  Palindrome or not "string"
"""
def fun(s,i):
    if i >= len(s) / 2:
        return True
    if s[i]!=s[len(s)-1-i]:
        return False
    return fun(s,i+1)
s="MADAM"
print(fun(s,0))"""