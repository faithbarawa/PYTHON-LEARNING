#items have to be unique, no duplication
#can be used to know the unique items by passing the set function
#print(set(name of list))
#not ordered
#one can check if an item is present---print(3 in name of set)
#union of sets(print(numbers1.union(numbers2)))
#number.remove/discard(item)
#numbers.add(item)
#intersection (numbers1.intersection(numbers2)) gives the values that are in both sets
#numbers1.difference(numbers2) gives the values that are in numbers1 but not in numbers2 or -
#symetric difference (numbers1.symmetric_difference(numbers2)) gives the values that are in either of the sets but not in both


def main():
    numbers={x**3 for x in range(10)}
    print()

    numbers2={x**2 for x in range(28)}
    print()
    print(numbers)
    print()
    print(numbers2)
    print
    print(numbers.intersection(numbers2))
    print()
    print(numbers.difference(numbers2))
main()


