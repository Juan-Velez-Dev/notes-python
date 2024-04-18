""" Enumerate """

list = ['a', 'b', 'c']

for item in enumerate(list):
    print(item)

for index, item in enumerate(list):
    print(index, item)

for index, item in enumerate(range(50, 55)):
    print(index, item)

# Tupples

my_tupples = list(enumerate(list))
print(my_tupples)
