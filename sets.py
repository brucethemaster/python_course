# Sets - unordered collections of unique elements
set1 = {"1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"}  # creating a set

list1 = [11, 12, 13, 14, 15, 15, 15, 11]
string1 = "aaabcdeeefgg"

# creating a set from a list; removing duplicate elements; returns {11, 12, 13, 14, 15}
set1 = set(list1)

# creating a set from a string; removing duplicate characters; returns {'b', 'a', 'g', 'f', 'c', 'd', 'e'}; remeber that sets are UNORDERED collections of elements
set2 = set(string1)

len(set1)  # returns the number of elements in the set

11 in set1  # returns True; checking if a value is an element of a set

10 not in set 1  # returns True; checking if a value is an element of a set

set1.add(16)  # adding an element to a set

set1.remove(16)  # removing an element from a set

# Frozensets - immutable sets. The elements of a frozenset remain the same after creation.
fs1 = frozenset(list1)  # defining a frozenset

fs1
frozenset({11, 12, 13, 14, 15})  # the result

type(fs1)
<class 'frozenset' >  # the result

# proving that frozensets are indeed immutable
fs1.add(10)
AttributeError: 'frozenset' object has no attribute 'add'

fs1.remove(1)
AttributeError: 'frozenset' object has no attribute 'remove'

fs1.pop()
AttributeError: 'frozenset' object has no attribute 'pop'

fs1.clear()
AttributeError: 'frozenset' object has no attribute 'clear'

#Sets - methods
set1.intersection(set2)  # returns the common elements of the two sets

set1.difference(set2)  # returns the elements that set1 has and set2 doesn't

# unifying two sets; the result is also a set, so there are no duplicate elements; not to be confused with concatenation
set1.union(set2)

set1.pop()  # removes a random element from the set; set elements cannot be removed by index because sets are UNORDERED collections of elements, so there are no indexes to use

set1.clear()  # clearing a set; the result is an empty set


set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set1.add(500)

print(set1)


set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set1.remove(7)

print(set1)


set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

set2 = {2, 4, 6, 9}

print(set1.difference(set2))


set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 19}

set2 = {0, 2, 4, 6, 9, 11, 14}

x = set1.intersection(set2)

print(x)
