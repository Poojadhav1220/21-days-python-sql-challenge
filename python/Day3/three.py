# print countdouwn
num=int(input('Enter a number: '))
while num>=1:
    print(num)
    num-=1

#print pattern
# 1
# 22
# 333
# 4444
# 55555
n=1
while n<=5:
    w=1
    while w<=n:
        print(n, end=' ')
        w+=1
    print()
    n+=1


# upside down pattern rightangle triangle *
# ******
# *****
# ****
# ***
# **
# *
n=int(input('enter a number: '))
while n>=1:
    w=1
    while w<=n:
        print('*', end=' ')
        w+=1
    print()
    n-=1


#fiboo
num=int(input('Enter a number: '))
count=0
a,b=0,1
while count < num:
    print(a, end=' ')
    a,b=b,a+b
    count+=1

#GCD 
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
while b!=0:
    a,b=b, a%b
print('GCD is: ',a)