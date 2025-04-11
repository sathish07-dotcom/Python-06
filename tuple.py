
# **Tuples in Python (20 Examples)**  
### **Basic Tuple Problems**
### **1. Create a Tuple and Print It**

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)


### **2. Access an Element in a Tuple**

my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])


### **3. Tuple Unpacking**

my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a, b, c)


### **4. Count the Occurrences of an Element**

my_tuple = (1, 2, 2, 3, 4, 2)
print(my_tuple.count(2))


### **5. Find the Index of an Element**

my_tuple = (10, 20, 30, 40)
print(my_tuple.index(30))



### **Intermediate Tuple Problems**
### **6. Convert a Tuple to a List**

my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)


### **7. Convert a List to a Tuple**

my_list = [4, 5, 6]
my_tuple = tuple(my_list)
print(my_tuple)


### **8. Check If an Element Exists in a Tuple**

my_tuple = ("apple", "banana", "cherry")
print("banana" in my_tuple)


### **9. Merge Two Tuples**

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)


### **10. Find the Maximum and Minimum in a Tuple**

my_tuple = (3, 7, 1, 9, 12)
print("Max:", max(my_tuple))
print("Min:", min(my_tuple))



### **Advanced Tuple Problems**
### **11. Find the Length of a Tuple**

my_tuple = (10, 20, 30, 40)
print(len(my_tuple))


### **12. Find the Sum of a Tuple**

my_tuple = (1, 2, 3, 4, 5)
print(sum(my_tuple))


### **13. Reverse a Tuple**

my_tuple = (1, 2, 3, 4)
print(my_tuple[::-1])


### **14. Tuple with Single Element**

single_element_tuple = (5,)
print(single_element_tuple)


### **15. Create a Nested Tuple**

nested_tuple = (1, 2, (3, 4), (5, 6))
print(nested_tuple)



### **Real-World Tuple Problems**
### **16. Iterate Over a Tuple**

my_tuple = ("a", "b", "c")
for item in my_tuple:
    print(item)


### **17. Tuple Comprehension Using Generator**

squared_tuple = tuple(x**2 for x in range(5))
print(squared_tuple)


### **18. Convert a String to a Tuple**

s = "hello"
char_tuple = tuple(s)
print(char_tuple)


### **19. Check If Two Tuples Are Equal**

t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 == t2)


### **20. Swap Two Variables Using Tuples**

a, b = 5, 10
a, b = b, a
print(a, b)


