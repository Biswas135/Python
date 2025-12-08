collection = set()               # create an empty set

collection.add(1)                # add integer 1
collection.add(2)                # add integer 2
collection.add("hello")          # add string "hello"
collection.add("world")          # add string "world"
collection.add((1, 2, 3))       # add a tuple (tuples are immutable, so allowed)

# collection.add([1, 2, 3])     # ❌ this would cause an error because lists are mutable and cannot be added to a set

print(collection)                # print the set
