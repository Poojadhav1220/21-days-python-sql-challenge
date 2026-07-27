'''1 Create an iterator manually from a list using iter() and pull out each value with next() in a loop,
catching StopIteration.'''
lst = [1,2,3,4,5,6,7,8,9,10]
itr=iter(lst)
try:
    while True:
        print(next(itr))
except StopIteration:
    pass

# 2 Write a generator function that yields numbers 1 to 100 one at a time.
def num():
    for i in range(1,101):
        yield i
generate=num()

for i in generate:
    print(i)


'''3 Write a generator function that yields infinite even numbers starting from 2 (test it by pulling only
the first 10 with next() or itertools.islice).'''
def even():
    n=2
    while True:
        yield n
        n+=2
generate=even()

for i in range(10):
    print(next(generate))

# 4 Write a generator expression (not a function) that yields the squares of numbers 1 to 10.
gen = (i*i for i in range(1,11))
for i in gen:
    print(i)

'''5 Explain in a code comment: why would you use a generator instead of returning a full list for a
sequence of 10 million numbers'''
# A generator creates one value at a time,
# so it uses much less memory.
# A list stores all 10 million numbers in memory at once,
# which requires much more memory.