#write a function is_prime that returns true/false
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(7))
print(is_prime(4))


'''Write a function greet(name, greeting='Hello') that returns a greeting string, demonstrating a
default argument, called both with and without the second argument.'''

def greet(name,greeting='Hello'):
    return f'{greeting} {name}'
print(greet('Pooja')) #using default argument
print(greet('Aditya', 'How are you?')) #using custom 2nd  argument

#Write a function sum_all(*args) that accepts any number of numbers and returns their sum
def sum_all(*args):
    # return sum(args) using built-in function
    total=0
    for i in args:
        total+=i
    return total
print(sum_all(10,20,30))

'''Write a function describe_person(**kwargs) that accepts any number of keyword arguments and
prints them as 'key: value' pair'''
def describe_person(**kwargs):
    result=[]
    for key,value in kwargs.items():
        result.append(f'{key}: {value}')
    return '\n'.join(result)
print(describe_person( name='Pooja', age=22, city='Mumbai'))

'''Write a function factorial(n) using a loop (not recursion), and a separate function
factorial_recursive(n) using recursion. Compare them mentally — which is easier to read?'''
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print(factorial(5))

def factorial_recursive(n):
    if n<=1:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(5))
