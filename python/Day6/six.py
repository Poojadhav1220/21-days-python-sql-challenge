# 1 Write a list comprehension to generate numbers 1 to 20.
numbers = [num for num in range(1,21)]
print(numbers)

# 2 Write a list comprehension to get the squares of numbers in a given list.
squares = [num**2 for num in numbers]
print(squares)

# 3 Write a list comprehension to extract only the vowels from a given string.
vowels = [char for char in "Hello World" if char in 'aeiouAEIOU']
print(vowels)

# 4 Write a dict comprehension that maps each word in a sentence to its length.
sentence = "This is a sample sentence"
word_len = {word : len(word) for word in sentence.split()}
print(word_len)

# 5 Write a set comprehension to get all unique vowels used in a given paragraph.
paragraph = "The morning sun rises softly in the sky and brings a warm, golden light to the world. Small birds sing happy songs in the green trees, and a cool breeze moves through the quiet streets. It is a peaceful time to drink a hot cup of tea, take a slow walk outside, and get ready for a bright new day"
unique_vowels = {vowel for vowel in paragraph if vowel in 'aeiouAEIOU'}
print(unique_vowels)