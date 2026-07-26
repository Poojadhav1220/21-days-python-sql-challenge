# Redo the leap year checker (Day 1) and the factorial function (Day 4) from scratch, no notes.
leap_year = int(input('enter a year:'))
if leap_year % 4 == 0 and leap_year % 100 !=0 or leap_year % 400 == 0:
    print(f'{leap_year} is leap year')
else:
    print(f'{leap_year} is not Leap year')

def factorial(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    return fact
print(factorial(5))    

''' Pick one comprehension from Day 6 and rewrite it as a plain for-loop, then compare which is more
readable — write a 2-line note on why.'''

vowels = [char for char in "Hello World" if char in 'aeiouAEIOU']
print(vowels)

vowels=[]
for char in "Hello World":
    if char in 'aeiouAEIOU':
        vowels.append(char)
print(vowels)

'''The list comprehension is more readable bacuase 
it is easier to understand and also 2 lines of code
while the for loop is 4 lines of code and also it is little
bit complex to understand.'''