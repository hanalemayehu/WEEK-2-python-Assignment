# 1.Create an empty list called my_list.
my_List = []

# 2.Append the following elements to my_list: 10, 20, 30, 40.
my_List.append(10)
my_List.append(20)
my_List.append(30)
my_List.append(40)

# 3.Insert the value 15 at the second position in the list.
my_List.insert(1, 15)

# 4.Extend my_list with another list: [50, 60, 70].

my_List.extend([50, 60, 70])

# 5. Remove the last element from my_list.
my_List.pop()

# 6.Sort my_list in ascending order.
my_List.sort()

# 7. Find and print the index of the value 30 in my_list.
index_30 = my_List.index(30)
print("Index of 30:", index_30)

#print final list

print("final list:", my_List)
