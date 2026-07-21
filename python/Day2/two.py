# sum of all digits
num=(input('Enter a number: '))
sum=0
for i in num:
    sum+=int(i)
print('sum of all digits is:',sum)

# reverse a string
str=input('enter a string: ')
rev=''
for i in str:
    rev=i+rev
print(rev)

#count of vowels in a string
str=input('enter a string: ')
count=0
for i in str:
    if i in 'aeiouAEIOU':
        count+=1
print('count of vowels in string is: ',count)

#multiplication table
num=int(input('Enter a number: '))
for i in range(1,11):
    print(f'{num} x {i} = {num*i}')

#factorial
num=int(input('Enter a number: '))
fact=1
for i in range(1,num+1):
    fact=fact*i
print('factorial is : ',fact)
