fruits = ["apple", "banana", "cherry"]
animals = ["cat", "dog", "elephant"]

for i, item in enumerate(fruits):
    print(i, item)



#zipping=iterating through both lists at the same time

for fruit, animals in zip(fruits,animals):
    print(fruit, animals)

