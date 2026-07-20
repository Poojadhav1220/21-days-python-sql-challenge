#even odd
# num=int(input("Enter a number: "))
# if num%2==0:
    # print('Number is even')
# else:
    # print('Number is odd')

#leap year
# year=int(input('Enter a year: '))
# if year%4==0 and year%100!=0 or year%400==0:
    # print('Year is a leap year')
# else:
    # print('Year is not leap year')


#grading system
# marks=int(input('Enter ur marks: '))
# if marks>=90:
    # print('Grade A')
# elif marks>=75:
    # print('Grade B')
# elif marks>=50:
    # print('Grade C')
# else:
    # print('Grade F')

#vowel check at the start of the string
# char=input('enter a string: ')
# if char[0] in 'aeiouAEIOU':
    # print('yes its starts with vowel')
# else:
    # print('No its not starts with vowel')

#largest among three numbers
a=int(input('Enter first no.: '))
b=int(input('Enter second no,: '))
c=int(input('Enter third no.: '))
if a>=b and a>=c:
    print('a is largest')
elif b>=a and b>=c:
    print('b is largest')
else:
    print('c is largest')