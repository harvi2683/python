
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def is_key_present(x):
    if x in d:
        print('Key is present in the dictionary')
    else:
        print('Key is not present in the dictionary')


is_key_present(5)
is_key_present(9)

Adict = {'Mon': 3, 'Tue': 5, 'Wed': 6, 'Thu': 9}
print("The given dictionary : ", Adict)
check_key = "Wed"
if check_key in Adict.keys():
    print(check_key, "is Present.")
else:
    print(check_key, " is not Present.")




def returnSum(myDict):
    list = []
    for i in myDict:
        list.append(myDict[i])
    final = sum(list)

    return final


# Driver Function
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))



def Merge(dict1, dict2):
    return (dict2.update(dict1))


# Driver code
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This return None
print(Merge(dict1, dict2))

# changes made in dict2
print(dict2)



class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value


# Main Function
dict_obj = my_dictionary()

dict_obj.add(1, 'Geeks')
dict_obj.add(2, 'forGeeks')

print(dict_obj)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)



tuplex = ("tuple", False, 3.2, 1)
print(tuplex)

# Create a tuple with numbers
tuplea = 5, 10, 15, 20, 25
print(tuplex)
# Create a tuple of one item
tuplea = 5,
print(tuplex)

# create a tuple
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)
# tuples are immutable, so you can not add new elements
# using merge of tuples with the + operator you can add an element and it will create a new tuple
tuplex = tuplex + (9,)
print(tuplex)
# adding items in a specific index
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)
# converting the tuple to list
listx = list(tuplex)
# use different ways to add items in list
listx.append(30)
tuplex = tuple(listx)
print(tuplex)

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
str = ''.join(tup)
print(str)

tuplex = tuple("w3resource")
print(tuplex)
# use the len() function to known the length of tuple
print(len(tuplex))



color_set = set()
print(color_set)
print("\nAdd single element:")
color_set.add("Red")
print(color_set)
print("\nAdd multiple items:")
color_set.update(["Blue", "Green"])
print(color_set)

# Create a set
setn = {5, 10, 3, 15, 2, 20}
print("Original set elements:")
print(setn)
print(type(setn))
print("\nMaximum value of the said set:")
print(max(setn))
print("\nMinimum value of the said set:")
print(min(setn))

# Create a new set
num_set = set([0, 1, 2, 3, 4, 5])
print("Original set elements:")
print(num_set)
print("\nRemove 0 from the said set:")
num_set.discard(4)
print(num_set)
print("\nRemove 5 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 2 from the said set:")
num_set.discard(5)
print(num_set)
print("\nRemove 7 from the said set:")
num_set.discard(15)
print(num_set)

# Program to perform different set operations
# as we do in mathematics

# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};

# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference
print("Difference :", A - B)

# symmetric difference
print("Symmetric difference :", A ^ B)

# Python3 code to demonstrate working of
# Identical element summation in lists
# using sum() + zip()

# initialize lists
test_list1 = [5, 6, 10, 4, 7, 1, 19]
test_list2 = [6, 6, 10, 3, 7, 10, 19]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# Identical element summation in lists
# using sum() + zip()
res = sum(x == y for x, y in zip(test_list1, test_list2))

# printing result
print("Summation of Identical elements : " + str(res))

