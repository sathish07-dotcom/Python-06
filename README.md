
# 📘 Python Lists & Tuples – Quick Guide

## 📌 Introduction

Python provides two important **data structures** to store **collections of items**:  
🔹 `List` – **Mutable**, ordered collection  
🔹 `Tuple` – **Immutable**, ordered collection  

---

## 🟦 Lists

### ✅ What is a List?
A **list** is a collection of items which can be changed after creation.  
Lists are defined using **square brackets `[]`**.

### 🔹 Example:
```python
fruits = ['apple', 'banana', 'mango']
print(fruits[0])  # Output: apple
```

### ✅ Key Features:
- Mutable (can be modified)
- Supports mixed data types
- Allows duplicate elements
- Supports indexing and slicing

### 🛠 Common List Methods:
```python
append(), extend(), insert(), remove(), pop(), sort(), reverse(), index(), count()
```

### 🧪 Sample Code:
```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)  # [1, 2, 3, 4]
```

---

## 🟨 Tuples

### ✅ What is a Tuple?
A **tuple** is a collection of items that **cannot be changed** after creation.  
Tuples are defined using **parentheses `()`**.

### 🔹 Example:
```python
coordinates = (10, 20)
print(coordinates[1])  # Output: 20
```

### ✅ Key Features:
- Immutable (cannot be modified)
- Faster than lists
- Supports mixed data types
- Supports indexing and slicing

### 🧪 Sample Code:
```python
point = (1, 2, 3)
print(point[0])  # Output: 1
```

---

## 🆚 List vs Tuple

| Feature       | List             | Tuple            |
|---------------|------------------|------------------|
| Syntax        | `[]`             | `()`             |
| Mutability    | ✅ Mutable       | ❌ Immutable     |
| Performance   | Slower           | Faster           |
| Methods       | Many available   | Limited          |
| Use Case      | Dynamic data     | Fixed data       |

---

## 📎 When to Use?
- Use **lists** when your data can change (e.g., user inputs, dynamic data).
- Use **tuples** when your data should remain constant (e.g., coordinates, fixed options).

---

## 🧠 Pro Tip:
If you try to modify a tuple, Python will raise a `TypeError`:
```python
t = (1, 2)
t[0] = 10  # ❌ TypeError: 'tuple' object does not support item assignment
```

---

Happy Coding! 💻  
Let me know if you'd like this in a Markdown file format or as a PDF!
