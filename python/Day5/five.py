# 1 Write a lambda that adds 15 to a number passed to it.
add_15 = lambda num: num +15
print(add_15(10))

# 2 Write a lambda that returns both the square and cube of a number as a tuple.
square_cube = lambda num: (num**2, num**3)
print(square_cube(5))

# 3 Use map() with a lambda to square every number in a list [1,2,3,4,5].
num_list = [1,2,3,4,5]
square_lst = list(map(lambda num: num**2, num_list))
print(square_lst)

# 4 Use filter() with a lambda to keep only even numbers from a list of 1-20.
even_num = list(filter(lambda num: num%2==0, range(1,21)))
print(even_num)

''' 5 You have a list of tuples [('Aditya', 22), ('Meera', 18), ('Ram', 30)]. Sort it by age using sorted() with
a lambda as the key.'''
people = [('Aditya', 22), ('Meera', 18), ('Ram', 30)]
sorted_people = sorted(people, key=lambda age: age[1])
print(sorted_people)