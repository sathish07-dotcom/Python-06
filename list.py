
# **Lists in Python (20 Examples)**  
### **Basic List Problems**
### **1. Create a List and Print It**

my_list = [1, 2, 3, 4, 5]
print(my_list)


### **2. Access Elements from a List**

my_list = ["apple", "banana", "cherry"]
print(my_list[1])  # Output: banana


### **3. Update an Element in a List**

my_list = [10, 20, 30]
my_list[1] = 25
print(my_list)


### **4. Append an Element to a List**

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


### **5. Insert an Element at a Specific Position**

my_list = [1, 3, 4]
my_list.insert(1, 2)  # Insert 2 at index 1
print(my_list)




### **Intermediate List Problems**
### **6. Remove an Element from a List**

my_list = [1, 2, 3, 4]
my_list.remove(3)  # Removes the first occurrence of 3
print(my_list)


### **7. Pop an Element from a List**

my_list = [10, 20, 30, 40]
popped_element = my_list.pop(2)  # Removes element at index 2
print(popped_element)
print(my_list)


### **8. Reverse a List**

my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)


### **9. Sort a List in Ascending Order**

my_list = [5, 2, 8, 1, 9]
my_list.sort()
print(my_list)


### **10. Sort a List in Descending Order**

my_list = [5, 2, 8, 1, 9]
my_list.sort(reverse=True)
print(my_list)




### **Advanced List Problems**
### **11. Find the Maximum and Minimum in a List**

my_list = [3, 7, 1, 9, 12]
print("Max:", max(my_list))
print("Min:", min(my_list))


### **12. Find the Sum of a List**

my_list = [1, 2, 3, 4, 5]
print("Sum:", sum(my_list))


### **13. Count the Occurrences of an Element**

my_list = [1, 2, 3, 1, 1, 4]
print(my_list.count(1))


### **14. Check if an Element Exists in a List**

my_list = ["apple", "banana", "cherry"]
print("apple" in my_list)  # Output: True


### **15. Convert a String to a List**

s = "hello"
char_list = list(s)
print(char_list)




### **Real-World List Problems**
### **16. Merge Two Lists**

list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)


### **17. List Comprehension to Square Elements**

numbers = [1, 2, 3, 4]
squares = [x**2 for x in numbers]
print(squares)


### **18. Remove Duplicates from a List**

my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(my_list))
print(unique_list)


### **19. Find Common Elements in Two Lists**

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common_elements = list(set(list1) & set(list2))
print(common_elements)


### **20. Flatten a Nested List**

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in nested_list for item in sublist]
print(flat_list)


